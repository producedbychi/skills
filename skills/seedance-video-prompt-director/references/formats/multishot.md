# Multi-shot format

Multiple distinct beats inside a single Seedance generation, ordered as numbered shots with a clear escalation arc. Use this when your scene needs visible cut-to-cut progression.

---

## When to use

- Transformations (calm → threat → transformation → aftermath)
- Multi-environment scenes that need cuts to navigate
- Process / journey narratives across distinct moments
- Action sequences with multiple beats (build-up, confrontation, resolution)
- Commercial scenes that need to show breadth of capability across multiple beats

Default to multi-shot for any scene over 6 seconds that has more than one distinct moment. The most flexible format.

---

## Structure

```
[Cinematic opening line — establishes visual quality bar]

[Subject + environment + atmosphere paragraph — what's in the world]

Shot 1: [shot description, ending in a clear cut point]

Shot 2: [shot description, re-anchored, contrasting in shot size and camera character]

Shot 3: [...]

Shot 4: [...]

[Optional SFX block]

[Optional negative prompt block]

Total: [Xs] / [N shots] / [aspect ratio]
```

---

## Cinematic opening line patterns

The opening line establishes the visual quality bar. Pick one and customize:

- "Montage, multi-shot action Hollywood movie, don't use one camera angle or single cut, cinematic lighting, photorealistic, 35mm film quality, professional color grading, sharp focus, high detail texture, film grain, depth of field mastery, ARRI ALEXA aesthetic"
- "Cinematic stylized 3D animation matching the keyframe, photorealistic environment particle simulation, volumetric atmosphere, [genre] energy, 2.35:1 widescreen, 24fps"
- "Editorial commercial cinematography, premium product realism, soft directional light, RED Komodo aesthetic, controlled color grade, high resolution"
- "Hyper-cinematic action realism, ARRI ALEXA Mini, anamorphic 35mm, dynamic handheld camera, Snyder-style speed-ramping, high contrast color grade"

For your specific genre, pull the opening line from `references/genres/<genre>.md`.

---

## Shot count by duration

- **4–7 seconds:** 2–4 shots. Tight, punchy.
- **8–11 seconds:** 4–6 shots. Standard multi-shot range.
- **12–15 seconds:** 6–8 shots. Maximum cut density.

More than 8 shots in a 15-second generation and Seedance starts compressing beats unevenly. Consolidate before splitting.

---

## Each shot needs four elements

For every numbered shot, write:

1. **Shot size** (close-up, medium, wide, ECU, etc.)
2. **Camera character** (handheld, locked-off, tracking, crane, etc.)
3. **Subject + action** (kinetic verbs, what happens)
4. **Atmosphere** (environment cue, light, particulate, mood)

Example:

> Shot 3: Wide low-angle as the chef plants both feet, swings the cleaver upward in a clean arc, the carrot SHEARS in two and tumbles outward. Steam rises from the pot beside her, lit by the warm overhead pendant.

That's all four: wide low-angle (shot size), implied stable / handheld (camera), plants feet + swings + shears + tumbles (subject + action), steam + warm pendant (atmosphere).

---

## Escalation arc

Multi-shot prompts read best when the shots build to a peak. The Higgsfield Burger / Bus / Cowboy structure is a useful default:

1. **Calm establishing** — sets the world and the protagonist's relaxed state
2. **Threat introduction** — disruptor appears, protagonist notices
3. **Transformation / response** — protagonist responds, the moment of transformation
4. **Climax** — the response peaks, often with VFX or impact
5. **Aftermath** — calm returns, the world is changed

You don't need exactly 5 beats — compress or expand based on duration. But the arc should escalate: each shot has more energy than the previous one until the climax beat, then releases.

---

## Verb density per shot

Each shot description should be packed with kinetic verbs. State verbs (sits, holds, looks) describe what's there; kinetic verbs (drops, sprints, snaps, lurches) describe what's happening.

**Sparse (fix this):**
> Shot 2: Wide shot as the zombie approaches the truck. The girl notices him.

**Dense (do this):**
> Shot 2: Wide shot of the concrete channel as the zombie BURSTS from the shadows under the bridge, sprinting with jerky unnatural strides across the dry riverbed toward the truck. Camera SHAKES tracking the approaching threat. The girl's eyes flick up from her burger.

The dense version has 6 kinetic verbs (bursts, sprinting, strides, shakes, tracking, flick) versus the sparse version's 2 (approaches, notices).

---

## Camera grammar variety per shot

Vary the camera character beat by beat. If Shot 1 is handheld, Shot 2 should NOT be handheld. If Shot 3 is locked-off, Shot 4 should NOT be locked-off. The variety creates rhythm.

A 6-shot 15-second prompt should use at least 4 different camera modes across its 6 shots.

---

## Re-anchoring at every cut

After every shot, the next shot must re-anchor:
- Where are we? (location relative to previous shot)
- Who's in frame and where?
- What direction do they face?
- What are they holding / what's in their hands?

Without re-anchoring, characters teleport and continuity breaks. See `references/cut-rules.md` for the full rule.

---

## VFX brackets inline

When a shot includes a specific visual effect, mark it with inline brackets:

> Shot 4: Medium close-up on the roof as green energy ribbons spiral up her body [VFX: glowing armor plates snapping onto her limbs and torso piece by piece, visor locking over her eyes, cannon assembling on her arm]. Camera circles tight, jolting with each plate impact.

The bracket separates the VFX direction from the action description. Seedance reads the bracket as a special instruction for that beat.

---

## SFX block (optional)

For action / drama / music-aligned scenes, append an SFX block at the end describing the audio energy of each beat. Even if Seedance generates the audio natively, the SFX block guides the model's energy peaks.

```
SFX: [shot 1 sound], [shot 2 sound], [shot 3 sound], [climax shot sound], [aftermath sound]
```

Example:

```
SFX: ambient burger eating, distant zombie skitter, sudden snarl, bone-cracking transformation, jaw-unhinging swallow, satisfied chewing return.
```

For commercial / product / process scenes where audio doesn't carry dramatic weight, you can omit the SFX block.

---

## Total footer

Always end with:

```
Total: 15s / 6 shots / 16:9
```

Replace with actual values. The footer tells Seedance the total duration, the number of shots you've described, and the aspect ratio. It's the engine's confirmation that you and the prompt agree on the budget.

---

## Full example skeleton

```
Cinematic action realism, ARRI ALEXA aesthetic, 35mm anamorphic, controlled color grade with deep shadows. Industrial Noir palette transitioning to warm tungsten on the climax beat.

A sprinter in a charcoal track suit rounds a stadium turn at full speed, breath fogging in the cold air, a single empty bleacher behind her. Steam rises from a vent at the far edge of the track.

Shot 1: Wide stabilized tracking parallel to the runner as she rounds the turn, body angled inward, shoulders driving forward, feet pounding the rubber surface in steady rhythm. Bleachers blur past in the background.

Shot 2: Cut to extreme close-up macro of her right foot as it strikes the track, the spike biting the surface, micro-debris kicking up. Slow-motion punctuation.

Shot 3: Cut to low-angle handheld as she enters the straight, body unwinding from the turn, arms beginning their drive forward. Camera shudders with the impact of her steps. Speed ramps from slow-motion back to real-time across this shot.

Shot 4: Cut to high-angle aerial drone descent toward the runner from above, revealing the empty stadium scale around her. The single illuminated track lane she's running glows against the dark surrounding lanes.

Shot 5: Cut to medium close-up locked-off on her face as she crosses the finish, breath punching out in a single visible cloud. Eyes lock straight ahead, jaw tight. The stadium clock in the corner of frame ticks one more digit and locks.

SFX: rhythmic spike strikes on rubber, breath puffs in cold air, distant stadium hum, slow-motion stretched footstep on impact, real-time return on the recovery, finish-line clock click, single bell tone.

Total: 12s / 5 shots / 16:9
```
