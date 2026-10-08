---
title: "Adding Life to The Forest At Night"
date: 2026-10-05
tags: ["the-forest-at-night", "game-development", "devlog"]
categories: ["the-forest-at-night"]
---

{{< figure src="images/junkerland-run.webp" alt="The boy running along a path through Junkerland, past junk piles, bare trees and crows" caption="Running through Junkerland, one of the new biomes." >}}

With the release of my current game **The Forest At Night** aimed for Halloween 2026, I'm going to be posting more about it as I finish it off.
This is a game about a young boy who leaves his house to venture into the forest at night-time, and sees it in a different light along the way.
It's an infinite runner rogue-like where you uncover the secrets and history of the forest as you go.

The last few weeks have been really great for the game as I've been working on finishing touches, polish and new content! It's nice to see it coming together!

## Scenes

One of the biggest changes is the ability to insert scenes into the gameplay world.
These are just simple environments and objects for now, which use the game's transparent dotty art style to help them look interesting.
I built a number of placeholder scenes just to make sure they look how I expect in the world, for example this Stonehenge-looking thing.

{{< figure src="images/stone-circle-middle.webp" alt="The boy standing in the middle of a ring of standing stones around a bird statue" caption="The early starting area, before the house went in. A ring of standing stones around a bird statue." >}}

These scenes really help bring the forest to life, as before it was nothing but endless paths.

I also added this cool rain effect to the objects placed into the world when it's raining.

{{< figure src="images/rain-on-house.webp" alt="Rain running down the walls of the house in the dotted art style" caption="Water running down the walls of the house in a downpour." >}}

I really want this to be a game with attention to detail, and I've always thought that these sorts of effects really help sell a game.
I'll be building more scenes and fleshing out the places in the forest in the coming weeks.

### Starting House

This game starts in a loop where the player leaves their bedroom, exits the house and runs into the forest.
Because of this, one of the most important areas was the house scene in which the player starts.

{{< figure src="images/starting-house.webp" alt="The boy standing on the garden path in front of the house at night" caption="The starting house, where every run into the forest begins." >}}

The player would end up seeing it every time they played the game, so it had to look good.
The idea for this game is that the forest is one you would normally see in our world, but seen through the eyes of a young child.
So, the house has to look pretty normal.

I never really liked modelling, so I'm actually quite happy the frontier models have got quite good at it recently, especially for things like architecture.
This house was built by giving GPT Astra (Fable is too overpriced) a brief to make me three different suburban house designs with a nice front garden.
I picked the one I liked the most and refined it further.

{{< figure src="images/house-drafts-page.webp" alt="A web page comparing three house designs: a gabled cottage, a bay-fronted house and a sheltered courtyard" caption="The page GPT put together to compare its three house designs." >}}

This was also a great opportunity to try out my new level editor to start scattering some objects around the garden.

{{< figure src="images/level-editor-house.webp" alt="The level editor showing the house, garden walls, paving and trees, with a scene tree panel on the left" caption="The house and garden in the level editor." >}}

I'm really happy with how the finished house turned out!

## Blanket System

I've already said I want this to be a game about small touches, and this is probably the most complicated system I've made for such a small part of the game.
When the boy wakes up after losing, he's lying in his bed.
The plan was he'd do animations like holding his blanket over his face to make him seem scared in the night.
I had no idea how I was going to do the blanket animation though, as I was worried I was going to have to model it for each frame in Blender (boring).
After ignoring it for long enough, I eventually realised it might be easier to try and get Claude to develop a real physics simulation to keyframe each section of the blanket, and use vertex shaders to morph the mesh.

{{< figure src="images/blanket-baker-held-up.webp" alt="The blanket baker tool, showing the boy sitting up in bed holding the duvet with its simulated cloth grid" caption="The blanket baker, with the boy sitting up and holding the duvet in its baked position." >}}

The blanket baker was one of the coolest things I did for this project. I can pose the character in his different positions and then the system determines the blanket locations with realistic physics.
This honestly saved me loads of time, but also gave me a tiny existential crisis about how easily AI can write up an entire physics simulation for a throwaway tool.

{{< figure src="images/blanket-cover-face.webp" alt="The boy in bed pulling the duvet up over his face, then lowering it again" caption="The baked blanket in game, with the boy hiding under the duvet and then peeking back out." >}}

## Releasing in time for Halloween

I'm working on lots of other pieces including new biomes like Junkerland at the top of this post, trying to refine the combat system, and just generally making the game more interesting.
I'll talk about that next week though!

If you're interested to learn more about The Forest At Night then follow along on my socials [@OtherMythos](https://x.com/OtherMythos), and subscribe to my [YouTube channel](https://www.youtube.com/@othermythos)!
