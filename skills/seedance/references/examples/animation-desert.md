# Animation example: Desert Hero

A hero with white braided hair fights a colossal cosmic entity in a vast arid desert — absorbing its energy, using it against it, and ultimately returning it. Full arc: confrontation → discovery → climax → resolution. Single shot, 15 seconds.

This example demonstrates: stylized 3D animation with photoreal environment, segmented timing within a continuous shot, dense VFX integration, full transformation arc within a single 15s generation.

**Genre:** fantasy-action + cinematic-narrative (composed)
**Format:** animation
**Capability:** consistency-control (keyframe + style reference in one image)

---

## The prompt

```
@image is the first keyframe and style reference. Cinematic stylized 3D animation — photorealistic desert environment, stylized characters. Hero: young woman, white braided hair, blue sleeves and leggings, brown leather vest and belt pouch, light build — uses speed and agility. Monster: colossal cosmic entity — massive glowing spherical body radiating neon rainbow energy (green, pink, red, blue, orange), multiple long dark blue tentacles, small vicious face with green glowing eyes and wide mouth, surrounded by swirling dust storm. Setting: vast arid desert — red-brown rocky terrain, massive dust storm wall, dramatic split sky blue and storm grey. High FPS, realistic particle physics.

0–3s: WIDE SHOT from @image. Hero sprints directly at the monster — tiny against its colossal scale. Monster fires a tentacle down like a whip — hero slides under it, the impact craters the desert floor, shockwave of dust and debris. She bounces up, runs along the tentacle as it retracts, reaches the main body. Drives her fist into the glowing surface — rainbow energy repels her, blasts her backward 10 meters skidding across desert sand. She lands, digs in. Looks at her hand — it's glowing faintly. Realizes something.

3–6s: Hero charges again — this time ABSORBING the energy on contact instead of fighting it. Her blue sleeves begin pulsing with absorbed rainbow light. Monster fires two tentacles simultaneously — she grabs one with both hands, swings on it, uses momentum to launch herself at the second, grabs it mid-air. Now holding two tentacles — she pulls them together, ties them in a knot using her whole body as leverage. Monster confused — tentacles tangled. She runs up the knotted tentacles toward the face. Half-second slo-mo — her mid-air between tentacles, rainbow light streaming off her arms, the monster's glowing face filling the sky behind her — SMASH full speed.

6–9s: She reaches the monster's face — drives both glowing hands directly into its eyes. Massive rainbow energy discharge explodes outward — the monster screams, the sound sending visible ripples through the dust storm. It convulses — tentacles flailing wildly, smashing into the desert floor creating craters. She holds on as the face bucks and writhes. The absorbed energy in her arms surges — she releases it all at once directly into the monster's core. Explosion of pure white light from the impact point, rainbow colors fragmenting outward like shattered glass.

9–12s: The monster's rainbow energy begins flickering — unstable. It rears back, swelling larger — about to explode or unleash everything. Hero drops to desert floor, sprints away full speed. The monster's energy builds — visible pressure distorting the air around it, colors strobing. It RELEASES — massive omnidirectional energy shockwave tears across the desert, flattening everything, the dust storm wall blasting apart. Hero dives behind a rocky outcropping — the shockwave passes over, sand and light washing across the entire landscape. Silence.

12–15s: Hero emerges from behind the rock. The monster still floats — but smaller, dimmer, energy depleted. Its tentacles hang limp. It looks at her — green eyes flickering. She walks toward it slowly. Raises one glowing hand — still holding its energy. Holds it out toward the monster. The energy flows back — she returns it. The monster's colors restore softly, gently. It slowly descends toward the desert floor, tentacles settling. They face each other. A moment. Monster turns, drifts away across the desert into the remaining dust. She watches it go. Wind catches her white braid.

Cinematic stylized 3D animation matching @image, photorealistic desert particle simulation, volumetric dust storm, rainbow neon energy VFX, absorbed energy glow on character, realistic sand physics, fast dynamic cuts. 2.35:1, 24fps.

Total: 15s / 1 shot / 16:9
```

---

## Why this prompt works

**Style locked at top AND bottom.** Opens with "Cinematic stylized 3D animation — photorealistic desert environment, stylized characters." Closes with the same commitment "Cinematic stylized 3D animation matching @image, photorealistic desert particle simulation, volumetric dust storm, rainbow neon energy VFX." This bookend reinforces the aesthetic across the duration.

**Character + monster + setting paragraph.** Before the timed beats, the prompt describes the three primary visual elements in detail. This gives the model a clear ontology of what's in the world.

**Five timed segments forming a complete arc.** 0–3s establishes confrontation. 3–6s introduces discovery (energy absorption). 6–9s is the climax (energy release). 9–12s is the destruction beat. 12–15s is the resolution. Five clear story beats in 15 seconds.

**Specific verb density per segment.** Just segment 1 has: sprints, fires, slides, craters, shockwave, bounces, runs, retracts, drives, repels, blasts, skidding, lands, digs, looks, realizes. 16+ verbs in 3 seconds.

**VFX integration without explicit brackets.** "Rainbow energy explodes outward," "rainbow colors fragmenting outward like shattered glass," "energy shockwave tears across the desert" — the VFX is woven into the action prose rather than bracketed separately. This works for animation because the entire scene is VFX-heavy.

**Resolution beat doesn't escalate further.** Segment 5 (12–15s) is intentionally calmer than segment 4 (the explosion). The hero returns the energy, the monster departs, wind catches the braid. This is the cinematic-narrative modifier showing through — the climax has already happened, the resolution holds.

---

## What to learn from this prompt

- **Animation prompts use timestamped beats more aggressively than other formats.** Five segments in 15s, each with its own narrative arc, is normal for animation. The format breathes the most across detail.
- **Style lock at top AND bottom prevents drift.** Without the closing style line, animation can drift toward photoreal as the action intensifies. The closing commitment keeps the aesthetic.
- **One keyframe can serve as character + style reference.** "@image is the first keyframe and style reference" pairs both roles in a single reference. Common for animation.
- **The fight choreography has internal logic.** The hero loses → adapts → exploits → wins → resolves. Each beat has clear cause-and-effect. Action without internal logic reads as random combat; action with logic reads as story.
- **The "half-second slo-mo" is precisely placed.** Mid-air between tentacles, just before contact with the face. One slo-mo, perfectly timed, then SMASH back to speed.
