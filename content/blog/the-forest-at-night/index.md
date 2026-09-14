---
title: "The Forest At Night"
date: 2026-09-14
tags: ["the-forest-at-night", "game-development", "devlog"]
categories: ["the-forest-at-night"]
---

{{< figure src="images/forest-path-walk.webp" alt="The boy walking along a winding path through the forest at night" caption="The boy walking the path through the forest, passing bonfires along the way." >}}

As mentioned in a YouTube video I made a little while ago, I've started working on a series of smaller games to help build my skills as a game developer.
The first was **Cat Hatch: Idle Pet Game**.
That game was only really made to get some experience at launching a complete product on the App Store.
If you've got an iPhone you can [play it here](https://apps.apple.com/us/app/cat-hatch-idle-pet-game/id6768046282).

Since then I've started work on another game, one I'm calling **The Forest At Night**.
It's a game about a young boy who leaves his room in a dream and walks into the forest.

## The Game

Gameplay wise it's a procedurally generated infinite runner, where the paths winding through the forest continue indefinitely.
The player is attacked by crows, who seem to be appearing in the forest more and more.
They can make friends with haunted figures and admire the relics of the past.

{{< figure src="images/statue-look.webp" alt="The boy standing next to a crow statue, looking up at it" caption="Stopping to admire one of the statues that stand along the path." >}}

The game is really meant to give the player a mysterious feeling.
The premise is that it's derived completely from the boy's imagination, so he's interpreting the things that might exist in the forest through the eyes of a child.

The game is still heavily in development, although lots of the basic parts are in place.
I'm aiming to get it finished by the end of October, which isn't that long considering I've been working on it for about three months so far.

## Prototyping

I started development by creating a few different prototypes to hammer the art style home.

{{< figure src="images/forest-prototype-walk.webp" alt="An early browser prototype of a character walking through a point cloud forest" caption="One of the early art style prototypes, a character walking through a point cloud forest in the browser." >}}

I merged all this stuff together to make a playable prototype completely using web technology, before I started to move it into my game engine.
It's just easier that way to test it on different devices and platforms.
I had lots of fun doing this and eventually ended up with something I liked.

{{< figure src="images/path-prototype.webp" alt="The playable web prototype, a top down view of a path winding through the forest" caption="The playable web prototype. The winding path, the wisps and the sanity meter all started here." >}}

## Moving to the Engine

Since then I've been slowly integrating the prototype into my C++ engine, the avEngine.
I've been doing this slowly to make sure it gets polished properly and also works well enough.

{{< figure src="images/engine-crows.webp" alt="The engine version of the game, with crows diving at the player" caption="The engine version of the game. The crows telegraph their dives with an orange ring before they strike." >}}

The gameplay follows a loop where the player wakes up in bed, leaves the house and ventures into the forest.
When the player runs out of sanity they wake back up in the bed, ready to start again.
I really like this arc, and took a bit of time to give the bedroom scene some dynamic weather so you get a different scene each time you wake up.
I want this to be a game of attention to detail.

{{< figure src="images/bedroom-weather.webp" alt="The bedroom scene, with the weather outside the window changing from clear to heavy rain" caption="The bedroom, with the weather outside the window sweeping from clear through to heavy rain." >}}

## What's Next

The plan for the next week is to work on audio.
I'm going to be getting a proper audio producer to make some music for this game, which is exciting.
But as I haven't properly put music into any of my games I need to prototype what I actually need, which should be really fun.

I also recently made a YouTube video about this game (and while you're there, subscribe to my channel!).

{{< youtube 3wSo6Wal2e4 >}}

If you haven't come across this project before, it's part of a larger series of projects where I'm trying to make a really big game I had the idea for when I was a teenager (I'm in my late 20s now, how the time flies).
Right now I'm trying to build my skills with smaller projects, as this is going to be a long term job and given the rate of progress so far might take my entire life 😅
