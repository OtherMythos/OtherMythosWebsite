---
title: "Giant Sand Worms: First OlderQuest Boss Fight"
date: 2026-03-12
tags: ["olderquest", "game-development", "boss-design"]
categories: ["olderquest"]
---

## The First Boss Battle

Recently I've been working on the first boss fight for OlderQuest: the giant sand worms! They're inspired by the creatures in *Dune* — massive, otherworldly predators that feel genuinely threatening.

### Attack Patterns

I started with a single attack pattern where the worms emerge and chomp at the player.

#### Emergence Attack

![Worm performing a close-range chomp](images/worm-chomp.gif)

This felt too simple, so I added a secondary phase where the worms jump out of the ground in an arc, creating more dynamic combat.

#### Chomping Attack

![Worm jumping out of the ground](images/worm-jump-ground.gif)

### Visual Polish

The art style makes it easy to create impactful visuals quickly. I spent a good amount of time experimenting with the particle system to make the worm's emergence look convincing. The worms also chase the player with particle effects that communicate exactly what's happening.

#### Mobile Testing

Here's how the boss looks during mobile device testing:

![Worm interaction during mobile device testing](images/worm-mobile.gif)

### Future Work

The worms can't be killed yet (though they can definitely kill you). I still need to programme a death animation and implement some satisfying loot rewards.

That said, I'm really happy with how this encounter has turned out so far!