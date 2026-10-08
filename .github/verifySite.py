#!/usr/bin/env python3
"""Check a Hugo build of othermythos.com before it goes anywhere near the server.

    python3 .github/verifySite.py public --published published.csv

published.csv is the output of `hugo list published`. Exits non-zero, listing every
problem, if the build is missing pages, links to files that aren't there, or contains
paths that belong to the hand-managed parts of public_html.
"""

import argparse
import csv
import os
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urljoin, urlsplit

SITE = "https://othermythos.com/"

REQUIRED = [
    "index.html", "sitemap.xml", "index.xml", "styles.css", "icon.jpg", "app-ads.txt",
    "blog/index.html", "games/index.html",
]

# Live on the server but not built by Hugo. The build must never contain them (a deploy
# would overwrite them), but links into them are fine.
HAND_MANAGED = ["builds", "OlderQuest", "experiments", "test", "DesignDoc.pdf"]

FORBIDDEN_TEXT = ["localhost", "127.0.0.1", "http://othermythos.com", "{{<", "{{%"]
TEXT_TYPES = (".html", ".xml", ".css", ".js", ".txt", ".json")
LARGE_FILE = 25 * 1024 * 1024


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if not value:
                continue
            if name in ("href", "src", "poster"):
                self.links.append(value)
            elif name == "srcset":
                self.links.extend(part.split()[0] for part in value.split(",") if part.strip())


def handManaged(rel):
    return any(rel == p or rel.startswith(p + "/") for p in HAND_MANAGED)


def resolve(root, rel):
    """Return the file a site path is served from, or None."""
    path = os.path.join(root, rel)
    if rel == "" or rel.endswith("/") or os.path.isdir(path):
        path = os.path.join(path, "index.html")
    return path if os.path.isfile(path) else None


def sitePath(url, pageUrl):
    """Turn a link on pageUrl into a path relative to the site root, or None if external."""
    full = urljoin(pageUrl, url)
    parts = urlsplit(full)
    if parts.scheme not in ("http", "https") or parts.netloc != urlsplit(SITE).netloc:
        return None
    return unquote(parts.path).lstrip("/")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("public")
    parser.add_argument("--published", required=True)
    args = parser.parse_args()
    root = args.public
    problems = []
    warnings = []

    for rel in REQUIRED:
        path = os.path.join(root, rel)
        if not os.path.isfile(path) or os.path.getsize(path) == 0:
            problems.append(f"missing or empty: {rel}")

    with open(args.published, newline="") as f:
        pages = list(csv.DictReader(f))
    if not pages:
        problems.append("hugo list published returned no pages")
    for page in pages:
        rel = sitePath(page["permalink"], SITE)
        if rel is None:
            problems.append(f"{page['path']}: permalink {page['permalink']} isn't on {SITE}")
        elif not resolve(root, rel):
            problems.append(f"{page['path']}: no output at /{rel}")

    fileCount = 0
    for dirPath, dirNames, fileNames in os.walk(root):
        dirNames.sort()
        for name in sorted(fileNames + dirNames):
            full = os.path.join(dirPath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if name.startswith("."):
                problems.append(f"hidden file in build: {rel}")
            if handManaged(rel) and "/" not in rel:
                problems.append(f"build contains hand-managed server path: {rel}")
        for name in sorted(fileNames):
            full = os.path.join(dirPath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            fileCount += 1
            size = os.path.getsize(full)
            if size > LARGE_FILE:
                warnings.append(f"large file ({size // (1024 * 1024)} MB): {rel}")
            if not name.endswith(TEXT_TYPES):
                continue
            with open(full, encoding="utf-8", errors="replace") as f:
                text = f.read()
            for bad in FORBIDDEN_TEXT:
                if bad in text:
                    problems.append(f"{rel} contains {bad!r}")
            if name.endswith(".html"):
                links = LinkParser()
                links.feed(text)
                pageUrl = urljoin(SITE, rel)
                for url in sorted(set(links.links)):
                    if url.startswith("#"):
                        continue
                    target = sitePath(url, pageUrl)
                    if target is None or handManaged(target):
                        continue
                    if not resolve(root, target):
                        problems.append(f"{rel}: broken link {url}")

    for warning in warnings:
        print(f"warning: {warning}")
    for problem in problems:
        print(f"error: {problem}")
    print(f"{fileCount} files, {len(pages)} published pages, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
