# Multi-shot example: The Burger

A girl eating a burger on a truck hood transforms into a massive creature to devour an approaching zombie, then returns to human form and keeps eating. Dark comedy pacing with horror undertones. 6 shots, 15 seconds.

This example demonstrates: numbered shot structure, escalation arc (calm → threat → transformation → climax → return), high verb density per shot, varied camera character per shot.

**Genre:** action-intense + horror-thriller (composed)
**Format:** multishot
**Capability:** consistency-control (image references for character, truck, location, zombie)

---

## The prompt

```
Montage, multi-shot action Hollywood movie, don't use one camera angle or single cut, cinematic lighting, photorealistic, 35mm film quality, professional color grading, sharp focus, high detail texture, film grain, depth of field mastery, ARRI ALEXA aesthetic.

A pink-haired girl with glasses, cream top and jeans sits on the hood of a white pickup truck under a concrete overpass at dusk, casually eating a burger. A shallow river channel stretches behind her, power lines and distant bridges framing the golden sky. A pale zombie with wet dark hair, bruised eyes and a blood-stained white shirt sprints toward her from the shadows of the channel. The girl calmly sets down the burger, her body erupts into a massive pale tusked creature with elongated limbs and clawed hands, devours the zombie whole, then shrinks back to human form and picks up the burger. Handheld shake throughout, dark comedy pacing with horror undertones.

Shot 1: Medium shot of the girl sitting cross-legged on the truck hood, chewing the burger lazily, golden dusk light catching her glasses and pink hair. Camera sways gently, ambient and calm.

Shot 2: Wide shot of the concrete channel as the zombie bursts from the shadows under the bridge, sprinting with jerky unnatural strides across the dry riverbed toward the truck. Camera shakes tracking the approaching threat.

Shot 3: Close-up on the girl's face as she notices the zombie, chewing slows, eyebrows rise with mild annoyance rather than fear. She sets the burger down on the hood beside her.

Shot 4: Medium shot as the girl drops off the hood and her body violently expands and twists upward into the massive pale tusked creature, spine cracking, limbs stretching, jaws splitting open wide, towering over the truck. Camera jolts with each bone-snap of the transformation.

Shot 5: Wide low-angle as the creature lunges forward and catches the charging zombie in its enormous clawed hand, lifts it off the ground and swallows it whole in one grotesque bite, jaw unhinging. Camera shudders with the impact.

Shot 6: Medium shot as the creature rapidly shrinks back into the girl, standing calmly beside the truck. She hops back onto the hood, picks up the burger, takes another bite and keeps chewing as if nothing happened.

Total: 15s / 6 shots / 16:9
```

---

## Why this prompt works

**Cinematic opening line** establishes the visual quality bar in a single sentence ("ARRI ALEXA aesthetic"). The model uses this to lock the photographic register.

**Camera character variety per shot.** Six shots, six camera modes:
- Shot 1: Medium handheld, gentle sway
- Shot 2: Wide shake-tracking (different mode)
- Shot 3: Close-up locked-off-ish
- Shot 4: Medium with violent jolts
- Shot 5: Wide low-angle, shudder
- Shot 6: Medium calm

No camera mode repeats consecutively. This is the double-contrast rule applied per cut.

**Verb density per shot.** Shot 4 has 6+ kinetic verbs in two sentences (drops, expands, twists, cracking, stretching, splitting, towering). Shot 5 has 5+ (lunges, catches, lifts, swallows, unhinging). Action shots load up; calm shots are lighter.

**Escalation arc.** Calm (1) → threat (2) → recognition (3) → transformation (4) → climax (5) → return (6). The energy builds to shot 5 and releases on shot 6.

**Reference images implied.** The prompt mentions "pink-haired girl with glasses, cream top and jeans" and "white pickup truck" specifically — these would be 4 reference images (girl, truck, location, zombie) provided alongside the prompt. The prompt doesn't tag them with `@image1` etc. because the reference list is implicit — Seedance reads the visual descriptions and matches to the attached references.

For our skill's output style, you'd add the explicit `@` tags:

> Shot 1: Medium shot of the girl @image1 sitting cross-legged on the truck @image2 hood...

---

## What to learn from this prompt

- **The opening sentence carries enormous weight.** "Cinematic lighting, photorealistic, 35mm film quality, professional color grading" is the engine's anchor for tone. Every prompt should have this kind of opening commitment.
- **Don't write a setup shot.** Shot 1 starts with the girl already eating. Past characters established the scene; the prompt enters mid-action.
- **Each shot description is dense.** The shortest shot description (Shot 1) is 17 words; the longest (Shot 4) is 36 words. Both pack action.
- **The dark comedy register is in the language.** Phrases like "casually eating" "with mild annoyance rather than fear" "as if nothing happened" carry the tone. Without these, the prompt would be straight horror.
