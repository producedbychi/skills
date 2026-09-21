# POV / Orb example: Electro

First-person POV of a character with lightning powers fighting through a storm-soaked industrial ruin, culminating in destroying a colossal iron titan by overloading its core. Single continuous shot, 15 seconds.

This example demonstrates: hyper-chaotic handheld POV, hands always visible, dense VFX brackets, slow-motion punctuation, comprehensive SFX block.

**Genre:** action-intense + fantasy-action (composed)
**Format:** pov-orb
**Capability:** text-only with one image reference (the protagonist's hand visualization)

---

## The prompt

```
Single continuous shot, first-person POV perspective, the camera IS her eyes, hyper-chaotic handheld motion, completely unstabilized, violent raw human movement, constant micro-jitters, aggressive head swings, abrupt jerks, frequent over-rotation and harsh correction, moments of near motion blur loss, no smoothness at all, no stabilization, wide-angle lens (strong distortion), subtle chromatic aberration near frame edges, 15 seconds, her hands always visible in frame, no music only raw SFX, cinematic lighting, photorealistic, grounded realism, strong 35mm film look, heavy film grain, sharp but imperfect focus, noticeable focus breathing, motion blur on fast actions, halation on highlights, soft highlight rolloff, slightly desaturated tones, ARRI ALEXA aesthetic, practical VFX feel, minimal CGI look, natural imperfections.

In a storm-soaked industrial ruin, her hand snaps forward catching a crackling violet lightning sphere suspended between broken metal beams, electricity arcing violently between surfaces, she crushes it instantly — blinding energy surges through her fingers as fractal lightning veins explode across both forearms [VFX: branching electric circuits pulsing with white-blue current, sparks jumping between fingers], the ground trembles as enemies emerge — dozens of jagged obsidian creatures crawl rapidly across walls and ground, their glowing red cores flickering, while a colossal iron titan rises behind them, towering above ruined towers, its chest a massive rotating electromagnetic core crackling with energy, she lunges forward — first strike, she grabs a creature mid-leap and overloads it, its body bursting into a spray of glowing shards, second attack, she slams both hands down releasing a radial lightning surge that chains between multiple enemies, frying them mid-motion, the titan retaliates firing a massive beam of compressed energy, she sidesteps violently, catching the beam with one hand, redirecting it upward while sprinting straight at the titan, she runs up its collapsing body using magnetic pulls, reaches the core and drives both hands inside, unleashing a catastrophic surge, RAMPS TO SLOW MOTION as the core fractures, energy tearing outward in layered shockwaves, metal plates peeling away — SNAPS BACK, she rockets skyward, both lightning-glowing hands at frame edges, looking down as the titan collapses in a chain reaction explosion, electrical storms spreading across the battlefield below.

SFX: electric crackle, sphere hum surge, energy burst, crawling creature skitter, deep metallic titan rise, sharp discharge pop, lightning chain blast, slow-motion electric hum stretch, snap impact, beam charge roar, energy deflection crack, metal tearing, core overload rumble, slow-motion energy rupture, explosive collapse, upward blast whoosh, distant thunder roll, debris falling.

Total: 15s / 1 shot / 16:9
```

---

## Why this prompt works

**Comprehensive POV lockdown.** The opening sentence is over 100 words and EVERY MODIFIER MATTERS. The "hyper-chaotic handheld motion, completely unstabilized, violent raw human movement, constant micro-jitters, aggressive head swings, abrupt jerks, frequent over-rotation and harsh correction, moments of near motion blur loss, no smoothness at all, no stabilization" sequence is what locks Seedance to first-person rather than defaulting to cuts.

**Hands always visible.** Reinforced explicitly ("her hands always visible in frame"). The hands carry the kinetic energy — they're how the audience experiences the powers.

**VFX brackets at peak moments.** Two brackets, both at energy-deployment beats. They separate the special-effect direction from the action description.

**Verb density.** Single continuous paragraph but the verbs are dense: snaps forward, catching, crushes, surges, explode, trembles, emerge, crawl, rises, towering, lunges, grabs, overloads, bursting, slams, releasing, chains, frying, retaliates, firing, sidesteps, catching, redirecting, sprinting, runs, reaches, drives, unleashing, fractures, tearing, peeling, rockets, looking down, collapses, spreading.

That's 30+ kinetic verbs in one paragraph. This is what action-intense register looks like at full deployment.

**Slow-motion punctuation.** "RAMPS TO SLOW MOTION as the core fractures..." with "SNAPS BACK" return. One ramp moment at the climax. The capitalized markers are explicit Seedance instructions.

**Dense SFX block.** Eighteen audio cues, time-aligned to the visual beats. The block guides the model's audio energy peaks even though Seedance generates audio natively.

---

## What to learn from this prompt

- **POV format requires verbose camera lockdown.** Don't trim the opening sentence — every modifier (constant micro-jitters, harsh correction, near motion blur loss) prevents the model from defaulting to smooth cuts.
- **VFX brackets pair best with kinetic verbs.** The bracket + verb combination ("she crushes it instantly — [VFX: branching electric circuits pulsing]") is more readable than describing the VFX in plain prose.
- **One slow-motion ramp per scene.** Use it at the climax. More than one and the prompt loses its punch.
- **The SFX block tells you the energy structure.** Reading the SFX block alone, you can map the scene's beats: build → engagement → climax → release. The visual prompt should match this audio energy structure.
