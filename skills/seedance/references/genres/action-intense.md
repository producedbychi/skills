# Action-intense

> **Lens note.** The camera stacks in this file are grade, stock and finish templates. Their millimeter values are legacy — convert the lens to a FOV degree from the ladder in `optics.md` before writing (`47° (50mm)`, `29° (85mm)`, `84° (24mm)`). Millimeters never lead, and apertures, ISO and lens brand names control nothing.


High kinetic energy, fast cuts, dense kinetic verbs, slow-motion punctuation at impact beats. Use as base genre for: fight scenes, chase sequences, transformation videos, high-action ad creative, viral hook content with explosive energy. Use as modifier for: any other genre where the user wants the energy register cranked up.

---

## Structural priorities (when used as base)

1. **Escalation arc is mandatory.** Calm → threat → engagement → climax → aftermath. The energy must build, then either release or hold.
2. **Impact beats are the visual peaks.** A single moment of contact (bullet meets target, fighter meets opponent, cluster meets surface) is the geometric center of the scene.
3. **Slow-motion at the impact beat.** Speed-ramp INTO the impact, hold the moment in slow-motion, snap back to real-time on the aftermath.
4. **Reaction inserts.** Show what the impact does — a face flooding with shock, dust kicking up, debris flying. Inserts are non-negotiable for action.

---

## Style declaration line patterns

- "Hyper-cinematic action realism, ARRI ALEXA Mini, anamorphic 35mm, dynamic handheld camera, Snyder-style speed-ramping, high contrast color grade, deep shadows, halation on highlights, 2.35:1 widescreen, 24fps."
- "Hollywood action cinematography, Sony Venice 2, 24mm wide for environmental action, 85mm for impact close-ups, controlled handheld with intentional shake, anamorphic flares, 2.35:1, 24fps."
- "Hard action realism, ARRI ALEXA, 35mm anamorphic, mixed handheld and stabilized, Industrial Noir grade desaturation, motion blur on fast actions, heavy grain, 2.35:1, 24fps."
- "Guy Ritchie speed-ramping with Snyder impact slow-motion, anamorphic 35mm, shallow depth of field, harsh single-source overhead industrial light casting deep dramatic shadows, warm amber tone on skin with cool steel-blue environment, 16:9."

---

## Verb register (Tier 4 — High action, with Tier 5 at climax)

Default verbs: SLAM, SMASH, HURL, PIVOT, TEAR, RIP, GRAB, WRENCH, DRIVE, HAMMER, POUND, ROCKET, BARREL, TUMBLE, CRASH, SPILL, ERUPT, BURST, SPRAY, STRIKE, SHUDDER, RECOIL, RICOCHET, WHIP, LUNGE, LEAP, VAULT, SOAR, PLUMMET, DETONATE, EXPLODE, SHATTER, FRACTURE, RUPTURE, COLLAPSE.

Climax verbs (Tier 5): VAPORIZE, ANNIHILATE, OBLITERATE, DECIMATE, IMPLODE, COLLAPSE INWARD, DETONATE OUTWARD, ERUPT, BURST OUTWARD, RIP APART, TEAR THROUGH, SCATTER INTO, EXPLODE OUTWARD, SHOCKWAVE OUTWARD.

Use Tier 5 sparingly — once per scene at the actual climax. Past that and the prompt loses its punch.

---

## Camera grammar defaults

- **Establishing:** wide handheld or low-angle aggressive establishing
- **Action beats:** mixed handheld + stabilized + lateral track, varying per beat
- **Impact beats:** macro close-up at 85–100mm, often slow-motion
- **Reaction beats:** medium close-up handheld, snap-zoom in, pull-back on aftermath
- **Climax beats:** crash zoom or rapid pull-back on the explosion / impact / transformation

Camera character variety per beat is non-negotiable. A 15s action scene should use 5+ different camera modes across its 6–8 cuts.

---

## Cut frequency

- 7s scene: 4–5 cuts
- 11s scene: 6–7 cuts
- 15s scene: 6–8 cuts (max for a single Seedance generation)

Cut on motion peaks. Cut INTO motion peaks. The propulsive feel comes from the cut grammar, not just the verb density.

---

## Lighting defaults

- High contrast key with deep fill ratio
- Hard single source for dramatic shadows
- Practical sources motivating the light direction
- Anamorphic flares on every visible light source
- Volumetric beam effects (dust, smoke, atmosphere catching light)
- Color contrast: warm key on subject, cool environment

Avoid: flat overhead diffusion (reads commercial), soft ambient (kills drama), HDR-flat midtones (reads digital).

---

## Color grade

- Industrial Noir for environmental
- Warm amber on skin / hero highlights
- Deep crushed-but-not-clipped blacks
- Halation on highlights
- Slightly desaturated overall (with selective saturation on key elements — blood, flame, neon)
- Heavy grain (35mm film texture)

---

## Slow-motion punctuation

Speed ramps are the action genre's signature beat. Use the standard pattern:

> The bullet leaves the barrel — RAMPS TO SLOW MOTION as it spins toward her face, neon light catching its surface, every detail suspended. SNAPS BACK to real-time as her finger contacts the watch crown.

The capitalized "RAMPS TO SLOW MOTION" and "SNAPS BACK" are explicit Seedance markers. Keep them in caps. Use the pattern at exactly one peak moment per scene — overuse kills the effect.

---

## VFX brackets (heavy use)

Action-intense uses VFX brackets liberally:

- [VFX: explosive shockwave detonating outward in concentric rings]
- [VFX: muzzle flash burst, hot brass casing ejecting]
- [VFX: glass spider-webbing, fragments suspended in air]
- [VFX: dust cloud erupting on impact]
- [VFX: lightning chains arcing between two metallic points]
- [VFX: speed lines exploding radially in all directions]

Aim for 2–4 VFX brackets per scene at peak moments.

---

## Reaction inserts

Action without reaction reads as choreography on a stage. Insert reaction beats throughout:

- Face flooding with shock (eyes wide, mouth open, breath catching)
- Hand gripping the dashboard / weapon / railing in white-knuckle tension
- Dust settling on a still body, single particle drifting
- Smoke curling from a barrel after the shot
- A single brass casing tumbling on concrete
- Blood drop hitting white floor

Inserts are sub-second beats, often macro. They land between the major cuts and give the action emotional weight.

---

## SFX block (always for action)

```
SFX: [build-up sound], [threat introduction sound], [engagement sounds — multiple impacts], [climax explosion sound], [slow-motion stretched sound], [snap-back to real-time], [aftermath silence or low rumble].
```

Example:

```
SFX: distant thunder, slow boot crunch on gravel, sudden weapon click, multiple rapid impacts, glass shattering, slow-motion bullet whoosh stretched, snap-back to real-time, single brass casing tumbling on concrete, distant siren approaching.
```

---

## Negative prompt block (always include)

```
Negative: no watermarks, no subtitles, no text overlays, no logos, no slow lyrical music, no soft commercial lighting, no flat midtones.
```

---

## Composition with other genres

### As modifier on `commercial-product`
- Cranks the energy of a product video without losing product as hero
- The cluster DETONATES into the assortment, doesn't "settle on the surface"
- See `genres/commercial-product.md` for the full composition rules

### As modifier on `cinematic-narrative`
- Adds kinetic energy to a character-driven scene
- "Heat" / "Sicario" / "Mission Impossible: Fallout" register
- Camera stays craftful but verbs and pacing escalate

### As modifier on `horror-thriller`
- Cranks the pressure into release
- Slow-build dread that detonates into action
- "Get Out" final act, "Hereditary" climax pacing

---

## Composition stack examples

**"High action commercial"** = `commercial-product` + `action-intense`
- Product is hero, action energy applies to the path to the product
- Verb density Tier 4, but resolution beat is the product clean

**"Cinematic action"** = `cinematic-narrative` + `action-intense`
- Character drives the scene, action escalates the stakes
- Held character beats interleave with explosive impacts

**"Action horror"** = `horror-thriller` + `action-intense`
- Dread builds, then explodes into kinetic release
- Climax pacing favors tension peak then explosion

**"Viral high action"** = `viral-hook` + `action-intense`
- Hook in first 1.5s, action energy sustained throughout
- Vertical-friendly, fast-cut, designed for autoplay feed

---

## Common scenes

- Fight choreography (one vs one, one vs many)
- Chase sequences (vehicle, foot, parkour)
- Transformation moments (calm character becomes explosive force)
- Impact beats (single decisive contact)
- Confrontation reaches breaking point
- Explosion / detonation / collapse beats
- Hero entrances with kinetic energy
