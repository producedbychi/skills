# Music video / beat-matched

> **Lens note.** The camera stacks in this file are grade, stock and finish templates. Their millimeter values are legacy — convert the lens to a FOV degree from the ladder in `optics.md` before writing (`47° (50mm)`, `29° (85mm)`, `84° (24mm)`). Millimeters never lead, and apertures, ISO and lens brand names control nothing.


Beat-driven visual rhythm, widescreen composition. Use as base genre for: music videos, beat-aligned content, choreography videos, dance content, beat-driven ad creative, montage edits aligned to music.

---

## Structural priorities (when used as base)

1. **Cuts hit on beats.** The visual rhythm matches the audio rhythm. Cuts land on downbeats; sustained takes hold across phrase changes.
2. **Visual variety per beat.** Each beat brings a new visual — angle, location, subject, color, motion. Repetition of the same visual across multiple beats kills the rhythm.
3. **Widescreen composition.** Default to 2.35:1 anamorphic for cinematic music video; 16:9 for standard; 9:16 for vertical TikTok-music format.
4. **Performance + B-roll alternation.** Most music videos alternate between performance shots (artist visible, often singing or playing) and B-roll (story, atmosphere, visual concept).

---

## Style declaration line patterns

- "Music video cinematography, ARRI ALEXA Mini, anamorphic 35mm, widescreen 2.35:1, beat-aligned cuts, vibrant color grade, dramatic lighting, 24fps."
- "MV-style visual rhythm, RED Komodo, mixed handheld and stabilized, fast cuts on beats with held takes across phrase changes, premium color grade with hero color, 16:9 or 2.35:1, 24fps."
- "Beat-matched ad creative, controlled handheld camera, fast cut rhythm with dynamic energy, high-saturation color grade, 9:16 vertical or 16:9, 24fps."

---

## Verb register (Tier 3 with selective Tier 4)

snap, flick, jerk, whip, bounce, lurch, hop, leap, dart, sprint, dash, surge, pulse, throb, race, rush, charge, swerve, weave, plant, pivot, slam, hit, strike, drop (the beat).

Selective Tier 4 verbs at peak beats: ERUPT, SHATTER, BURST, COLLAPSE, SOAR.

Music video verbs are kinetic and rhythmic. Each verb should match a beat or a transition.

---

## Beat-cut patterns

### Standard 4/4 pacing
- 60 BPM = beat every 1.0s
- 80 BPM = beat every 0.75s
- 100 BPM = beat every 0.6s
- 120 BPM = beat every 0.5s
- 140 BPM = beat every 0.43s

For 15s of video at 120 BPM, that's ~30 beats. Cuts every 2 beats (1 second) is comfortable. Cuts every 4 beats (2 seconds) feels held. Cuts every 1 beat (0.5s) feels frenetic.

Match the cut frequency to the song's energy.

### Cut-on-beat language
When writing the prompt, signal beat alignment:

> 0–2s: Wide stabilized lateral track, dancer mid-pose. Cut on the downbeat.
>
> 2–4s: Snap zoom into the dancer's eyes (cut lands on the next downbeat). Hold for 4 beats through the chorus phrase.
>
> 4–6s: Cut to dancer's feet hitting the ground in time with the kick drum. Each subsequent cut is a different angle on the dance, snapped to the snare.

---

## Camera grammar defaults

- **Performance beats:** medium close-up on the artist, handheld with controlled motion, often pulling focus between artist and environment
- **B-roll beats:** wide stabilized environmental, lateral tracking, drone descents
- **Choreography beats:** wide stabilized to capture full body, mixed with low-angle close-ups for impact
- **Climax beats:** crash zoom, hyper-fast camera motion, dramatic angle change
- **Hold beats (across phrase changes):** locked-off or very slow stabilized push, lets the viewer breathe

---

## Lighting defaults

- Dramatic with strong color contrast
- Practical neon / colored LED visible in frame
- Anamorphic flares on every visible light source
- Backlight separating subject from background
- Selective color isolation (red light on subject, blue environment)

For traditional music videos: dramatic single-source key, deep shadows, halation. For modern viral music content: vibrant high-key with high saturation.

---

## Color grade

- High contrast with vibrant saturation
- Hero color isolation (one color holds, rest desaturates)
- Teal-and-orange or magenta-and-cyan for modern music video
- Black-and-white sections for emotional contrast (alternated with color)
- Anamorphic flares preserved in the grade

---

## Multi-image / multi-location patterns

Music videos often span multiple locations. Use the multi-image reference pattern:

> @image1 — first location (street performance)
> @image2 — second location (rooftop)
> @image3 — third location (warehouse interior)
> @image4 — final location (desert)
>
> The artist appears in each location as the song progresses. Transitions between locations on phrase changes (every 4 bars). Visual style holds consistent across all locations: anamorphic 2.35:1, dramatic lighting, hero color isolation.

The locations cut on phrase changes; the cuts within each location hit on individual beats.

---

## Beat-sync reference video

For matching the rhythm of an existing video (a viral dance, a previous music video):

> Reference @video1's beat-pacing. Cuts in this video should land on the same beats as @video1's cuts. Match the cut rhythm exactly. Do not match @video1's content — only its rhythm.

---

## Performance vs B-roll allocation

Standard music video allocation:
- 50% performance (artist on camera)
- 30% B-roll story / concept
- 20% atmospheric / abstract

For dance / choreography:
- 70% choreography
- 20% B-roll
- 10% atmospheric

For concept / narrative music video:
- 30% performance
- 50% narrative
- 20% atmospheric

State the allocation in the prompt or imply it through beat distribution.

---

## Sound design

For music videos, the audio direction is the music itself. The SFX block becomes a beat-alignment notation:

```
Music: Beat at 0s, 0.5s, 1s, 1.5s... Cuts align to downbeats. Held shots span phrase changes.
SFX: minimal — music is foreground. Footstep impacts on choreography beats may double the kick drum hits.
```

If the user provides an audio reference (`@audio1`):

> Music reference: @audio1. Match beat pacing to @audio1's structure. Cuts on downbeats, holds on phrase changes.

---

## Composition with other genres

### As modifier on `viral-hook`
- "Viral music content" — TikTok music-driven viral
- 9:16 vertical, hook in first beat, sustain through chorus

### As modifier on `cinematic-narrative`
- "Cinematic music video" — narrative-shaped music content
- Story unfolds across the song with cuts on beats

### As modifier on `action-intense`
- "Action music video" — high-energy beat-aligned action
- Cuts double-time the music; impact beats land on downbeats

### As modifier on `fantasy-action`
- "Fantasy music video" — VFX-heavy magical music content
- Spell deployments align to song peaks

---

## What this genre does NOT do

- Slow documentary observation
- Held silence (music carries it)
- Long single takes (music videos cut)
- Educational explanation
- Commercial product hero shots (music video isn't selling, it's expressing)

---

## Negative prompt block

```
Negative: no watermarks, no subtitles unless lyric overlays are explicitly part of the design, no slow pacing inconsistent with the music tempo, no commercial-bright lighting (unless brand-driven music content), no documentary restraint.
```

---

## Reference image style

- "Cinematic music video still photography, anamorphic 2.35:1, dramatic lighting, vibrant color grade with hero color isolation"
- "Performance still — artist mid-pose, dramatic key light, deep shadows"
- "B-roll still — environmental, atmospheric, beat-aligned composition"
- "Multi-location music video keyframe, dramatic dramatic lighting consistent with the music's mood"

---

## Common scenes

- Artist performing in a stylized environment (warehouse, rooftop, street)
- Dance / choreography sequence
- Narrative B-roll telling a story alongside the song
- Visual abstract / concept content (not literal narrative)
- Multi-location performance (artist in 3–5 locations across one song)
- Ensemble shots (band, dance crew, group choreography)
- Slow-motion impact beats aligned to the bass drop
- Lyric-on-screen treatment (lyrics composited in post over beat-aligned visuals)

---

## Vertical music video specifics (9:16)

For TikTok / Reels music content:
- Subject centered vertically in the frame
- Action stays within the vertical column
- Faces fill the upper third or center
- Performance shots have the artist closer to the lens than horizontal would prefer
- Cuts are faster than horizontal music video (every 0.5s for high-energy content)
- Hook in the first beat (0–0.5s) is mandatory

State 9:16 in the style line and footer.
