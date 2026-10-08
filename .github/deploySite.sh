#!/usr/bin/env bash
# Upload a verified Hugo build to othermythos.com's public_html over FTPS.
#
#   FTP_USER=u857925503.siteDeploy FTP_PASSWORD=... .github/deploySite.sh public [--dry-run]
#
# Only uploads: it never deletes anything on the server, so everything Hugo doesn't build
# (OlderQuest/, experiments/, builds/, ...) is left alone, and files with the same name are
# replaced. Assets go before pages, so a page never links to an image that isn't there yet.
#
# The FTP account's root is the whole hosting home (.ssh/, domains/, ...), so everything
# happens inside SITE_DIR, and only once it looks like the live site.
#
# Hostinger's FTP certificate is for *.hstgr.io, so ftp.hstgr.io must resolve to
# ftp.othermythos.com's address (the workflow adds it to /etc/hosts).
set -euo pipefail

SITE_DIR=/domains/othermythos.com/public_html

dir=${1:?usage: deploySite.sh <publicDir> [--dry-run]}
dryRun=${2:-}
[ -z "$dryRun" ] || [ "$dryRun" = "--dry-run" ] || { echo "unknown option: $dryRun" >&2; exit 2; }
: "${FTP_USER:?FTP_USER is not set}" "${FTP_PASSWORD:?FTP_PASSWORD is not set}"

[ -f "$dir/index.html" ] || { echo "$dir/index.html is missing; refusing to deploy" >&2; exit 1; }
for name in builds OlderQuest experiments test DesignDoc.pdf; do
    [ ! -e "$dir/$name" ] || { echo "$dir/$name exists; it would overwrite the server's copy" >&2; exit 1; }
done

# The cls aborts unless SITE_DIR has the build host and the wiki in it. In lftp the first
# filter sets the default, so the second mirror, which starts with an include, uploads only pages.
export LFTP_PASSWORD=$FTP_PASSWORD
lftp --env-password -u "$FTP_USER" ftp.hstgr.io <<EOF
set cmd:fail-exit true
set ftp:ssl-force true
set ftp:ssl-protect-data true
set ssl:verify-certificate true
set net:max-retries 3
set net:timeout 30
cd $SITE_DIR
cls builds/index.html OlderQuest/Wiki/Main_Page.html
mirror --reverse --no-perms --parallel=2 --verbose $dryRun --exclude-glob .* --exclude-glob *.html --exclude-glob *.xml "$dir" .
mirror --reverse --no-perms --parallel=2 --verbose $dryRun --include-glob *.html --include-glob *.xml --exclude-glob .* "$dir" .
EOF
