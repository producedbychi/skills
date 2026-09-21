# POV / Orb format

First-person locked perspective. The camera IS the character's eyes. No cuts, no zoom, only natural head movement. Use for immersive moments where the viewer experiences the scene directly through the protagonist.

---

## When to use

- Buyer's-eye-view sequences (commercial / explainer)
- First-person action (chase, fight, escape)
- POV ad creative ("orbs" — character with powers, hands always visible)
- Hero entrances where the audience needs to see what the protagonist sees
- Single-character moments where third-person would dilute the immersion

The Higgsfield "orb" is a specific subgenre: first-person character with VFX powers, both hands always visible, hyper-chaotic handheld motion. The format below covers POV in general; orb is a specialization with more specific rules.

---

## The locked perspective principle

POV / orb format is the strictest format in this skill. The single most important rule:

**Tell Seedance what the camera is NOT doing.** Without explicit negation, Seedance defaults to cutting between angles and the perspective breaks.

The required negation phrases:
- "No cuts."
- "No zoom."
- "Natural head movement only."
- "First-person POV throughout."
- "The camera IS [her/his/their] eyes."

Include all of these in the camera grammar declaration at the top of the prompt.

---

## Structure

```
[Cinematic opening line — establishes visual quality bar]

[Camera grammar declaration — explicit POV lockdown]

[Subject + environment + atmosphere paragraph]

[Continuous action description — beat by beat or as one flowing paragraph]

[Optional SFX block]

[Negative prompt block — usually included for POV]

Total: [Xs] / 1 shot / [aspect ratio]
```

---

## Camera grammar declaration patterns

Pick the intensity tier matching your scene:

### Calm / observational POV

> Single continuous shot, first-person POV perspective, the camera is the character's eyes. No cuts, no zoom. Natural head movement only. Stabilized handheld motion, gentle micro-shifts as the character looks around. Wide-angle lens with subtle distortion at frame edges.

### Active / kinetic POV

> Single continuous shot, first-person POV perspective, the camera IS her eyes. Handheld with constant micro-jitters. Aggressive head swings as the character reacts. No cuts, no zoom, no smoothness. Wide-angle lens with strong distortion. Hands visible in frame.

### Hyper-chaotic / orb POV

> Single continuous shot, first-person POV perspective, the camera IS her eyes, hyper-chaotic handheld motion, completely unstabilized, violent raw human movement, constant micro-jitters, aggressive head swings, abrupt jerks, frequent over-rotation and harsh correction, moments of near motion blur loss, no smoothness at all, no stabilization, wide-angle lens (strong distortion), subtle chromatic aberration near frame edges, her hands always visible in frame, no music only raw SFX, cinematic lighting, photorealistic, grounded realism, strong 35mm film look, heavy film grain, sharp but imperfect focus, noticeable focus breathing, motion blur on fast actions, halation on highlights, soft highlight rolloff, slightly desaturated tones, ARRI ALEXA aesthetic, practical VFX feel, minimal CGI look, natural imperfections.

The hyper-chaotic version is verbose because every modifier matters. Don't trim it — Seedance reads each phrase as a constraint.

---

## Hands always visible (orb)

For orb format specifically, hands stay in frame throughout. This is what makes the POV feel kinetic — the viewer can see what the character is doing with their hands at all times.

> Both hands visible at frame edges throughout. [VFX: lightning veins glowing across forearms, sparks jumping between fingers]. Hands react to the action — grip, release, strike, deflect.

For non-orb POV (a buyer at their desk, a runner mid-stride), hands appear when natural — typing, holding the steering wheel, reaching forward. Don't force hand visibility if it doesn't fit the scene.

---

## Action description structure

POV scenes can be written two ways:

### Pattern A — One flowing paragraph (orb / hyper-chaotic)

A single dense paragraph with multiple actions, no explicit beat boundaries. Seedance interprets the timeline from action density.

> In a storm-soaked industrial ruin, her hand snaps forward catching a crackling violet lightning sphere suspended between broken metal beams, electricity arcing violently between surfaces, she crushes it instantly — blinding energy surges through her fingers as fractal lightning veins explode across both forearms [VFX: branching electric circuits pulsing with white-blue current, sparks jumping between fingers], the ground trembles as enemies emerge — dozens of jagged obsidian creatures crawl rapidly across walls and ground...

This pattern is what Higgsfield's orb prompts use. Reads as a continuous experiential flow.

### Pattern B — Timestamped beats (calm / narrative POV)

Use timestamp markers like continuous format. Better for slower-paced POV (a buyer reviewing samples, a doctor moving through a hospital).

> 0–4s: Down at the cluttered desk, hand visible at the bottom of frame gripping a red felt-tip pen, supplier sprawl crowding the periphery.
>
> 4–8s: Head tilts up — the desk transformed, the same hand now relaxed, a single Hayden Valley case open with the assortment visible.

Pattern B is what your Hayden Valley Scene 1 uses (POV down at desk + reverse to the buyer's face). Pattern A is for high-energy single-take immersion.

---

## VFX brackets (orb-specific)

Powers, energy effects, and supernatural visual elements get inline brackets. Seedance reads these as separate VFX direction.

> Her right hand snaps upward [VFX: blue lightning chains arcing between her fingers and the metal ceiling], the sound rattles her teeth.

> Both palms slam together [VFX: white-hot shockwave detonating outward in concentric rings, debris vaporizing], the force throws her backward.

Bracket density: 1–3 brackets per scene. More than that and the prompt gets cluttered.

---

## SFX block (always for orb / often for POV)

POV / orb format is sound-driven — the experiential immersion depends on auditory cues. Always include an SFX block.

```
SFX: electric crackle, sphere hum surge, energy burst, crawling creature skitter, deep metallic titan rise, sharp discharge pop, lightning chain blast, slow-motion electric hum stretch, snap impact, beam charge roar, energy deflection crack, metal tearing, core overload rumble, slow-motion energy rupture, explosive collapse, upward blast whoosh, distant thunder roll, debris falling.
```

For calm POV, the SFX block is shorter:

```
SFX: ambient office tone, soft pen-tap, distant phone ringing, hand exhaling on polished wood, single calm room tone.
```

---

## Negative prompt block (always include for POV)

```
Negative: no watermarks, no subtitles, no text overlays, no logos, no on-screen graphics, no third-person cuts, no establishing shots, no aerial views.
```

The "no third-person cuts, no establishing shots, no aerial views" reinforces the POV lockdown.

---

## Slow-motion in POV

POV scenes with action benefit from speed ramps. Use the standard pattern:

> RAMPS TO SLOW MOTION as the bullet leaves the barrel — spinning, neon light catching its surface, drifting toward her face. SNAPS BACK to real-time as her finger contacts the watch crown.

In POV the slow-motion needs to feel motivated by the protagonist's experience (time slowing as adrenaline spikes), not by the editor.

---

## Total footer

```
Total: 15s / 1 shot / 16:9
```

POV is always 1 shot. The "shot" count is locked at 1 because there are no cuts.

---

## When NOT to use POV

POV doesn't work when:
- The scene needs multiple characters with their own coverage (POV only sees one POV)
- The protagonist's reactions are the dramatic content (you can't see your own face in POV)
- The scene depends on environmental scale that POV can't render (a vast battlefield reads better in third-person wide)
- The audience needs to see what the protagonist doesn't see (dramatic irony)

If the brief calls for any of these, switch to multi-shot or continuous and reserve POV for a specific beat within those formats.

---

## Hybrid POV + reverse

Sometimes a scene wants POV for immersion AND a reverse shot to show the protagonist's reaction. This is what your Hayden Valley Scene 1 does.

In this case, treat the scene as multi-shot format with POV beats inside it:

> Shot 1 (POV): Down at the cluttered desk, hand visible at the bottom of frame gripping the pen, supplier sprawl crowding the periphery. Fluorescent industrial cyan pall.
>
> Shot 2 (Reverse): Tight three-quarter reverse on the buyer, brow drawn tight, mouth turned down in tension, hand at the temple.
>
> Shot 3 (POV): Same first-person frame, the desk now transformed, hand relaxed, the Hayden Valley case open at center.

The POV format file applies to the POV beats. The multi-shot format file applies to the overall structure.

---

## Full example skeleton (orb)

```
Single continuous shot, first-person POV perspective, the camera IS his eyes, hyper-chaotic handheld motion, completely unstabilized, violent raw human movement, constant micro-jitters, aggressive head swings, abrupt jerks, frequent over-rotation and harsh correction, moments of near motion blur loss, no smoothness at all, no stabilization, wide-angle lens (strong distortion), subtle chromatic aberration near frame edges, his hands always visible in frame, no music only raw SFX, cinematic lighting, photorealistic, grounded realism, strong 35mm film look, heavy film grain, sharp but imperfect focus, noticeable focus breathing, motion blur on fast actions, halation on highlights, soft highlight rolloff, slightly desaturated tones, ARRI ALEXA aesthetic, practical VFX feel, minimal CGI look, natural imperfections.

In a collapsed cathedral overgrown with bioluminescent moss, his right hand reaches forward and presses against an ancient stone door, palm flat against its carved face, runes igniting beneath his fingers [VFX: green-blue light spiraling outward from each fingertip, runes activating in a chain reaction across the door's full surface], the door GROANS and shifts inward releasing a gust of cold air that rushes past his face, head jerks back from the wind, eyes snap open wider, both hands now visible reaching forward into the dark interior, footsteps echoing on stone as he advances inside, the moss dimming behind him, ahead a single shaft of pale light reveals a stone altar with a glowing crystal, his hands lift toward it [VFX: the crystal pulses in response, light reaching outward toward his palms], at one centimeter the crystal DETONATES outward in a pure white shockwave, hands reflexively raised, vision washing white, RAMPS TO SLOW MOTION as the shockwave passes through him, runes embedded in his forearms igniting [VFX: matching glow on his skin, particles rising from his arms], SNAPS BACK to real-time as he stands at the altar's edge, the crystal cradle empty, his hands still glowing faintly.

SFX: distant cathedral echo, stone groan, cold air rush, footsteps on stone, crystal hum rise, slow-motion white burst stretch, snap-back to real-time hush, faint rune-glow shimmer.

Negative: no watermarks, no subtitles, no text overlays, no logos, no third-person cuts, no establishing shots, no aerial views.

Total: 15s / 1 shot / 16:9
```
