# Music beat sync

Synchronize visual rhythm precisely with music beats. The Seedance capability for matching cuts, pacing, and energy to a music reference or specified BPM.

---

## When the user is in this capability

- "Sync the cuts to this music — use @audio1 as the rhythm reference."
- "Beat-cut visualization at 120 BPM."
- "Match the rhythm of @video1's edit pacing."
- "Music video where the visuals hit on every downbeat."

If the brief involves matching visual rhythm to audio rhythm, you're in beat-sync.

---

## Prompt structure

```
@image1 @image2 ... @imageN + Match @video1's beat pacing / Match @audio1's rhythm + [visual style] + [aspect ratio]
```

---

## With a music reference (@audio1)

> Music reference: @audio1. Match @audio1's beat structure exactly. Cuts in this video should land on @audio1's downbeats. Held shots should span @audio1's phrase changes (every 4 bars).

This tells Seedance the audio rhythm is the editorial spine.

---

## With a video reference (@video1)

When matching another video's pacing:

> Reference @video1's edit pacing. Cuts in this video should land at the same intervals as @video1's cuts. Match the cut rhythm exactly. Do NOT match @video1's content — only its rhythm.

---

## With explicit BPM

When neither audio nor video reference is provided:

> Beat-cut at 120 BPM. Cuts every 0.5 seconds (every beat). Held shots span 2 beats (1 second). Climax beat held for 4 beats (2 seconds).

State the BPM and the cut frequency explicitly.

---

## Multi-image beat-sync

When multiple images need to be cut into the rhythm:

> @image1 @image2 @image3 @image4 @image5 @image6 @image7 — these are the visual content. Each image gets approximately 2 seconds of screen time, cut on @audio1's downbeats. Style: dramatic music video aesthetic, anamorphic 2.35:1, vibrant color grade.

The images become the visual content; the audio becomes the cut spine.

---

## Common BPM references

| BPM | Cut every | Use for |
|---|---|---|
| 60 | 1.0s | Slow ballad, cinematic narrative |
| 80 | 0.75s | Mid-tempo, moody music video |
| 100 | 0.6s | Standard pop / hip-hop |
| 120 | 0.5s | Up-tempo dance / electronic |
| 140 | 0.43s | High-energy EDM / drum'n'bass |
| 160 | 0.38s | Hardcore / extreme energy |

For 15s of video at 120 BPM, that's 30 beats. Cuts every 1 beat = 30 cuts (too many for Seedance's ~8 cuts per generation cap). Cuts every 4 beats (every 2 seconds) = 7 cuts (achievable).

---

## Which beats to cut on

Standard patterns:
- **Cut on every downbeat (beat 1 of every bar)** — even, predictable, easy to follow
- **Cut on every kick drum hit** — adds weight to each cut
- **Cut on snare hits (beats 2 and 4)** — backbeat-driven, slightly more energetic
- **Cut on ALL beats (every quarter note)** — frenetic, hard to follow visually
- **Cut at phrase changes (every 4 or 8 bars)** — held takes that breathe with the music
- **Cut on dynamic shifts** — when the music's energy changes, the visual changes

For most music videos, cut on the kick drum hits (beats 1 and 3 of every 4/4 bar). It's punchy without being chaotic.

---

## Climax sync

Music has dramatic peaks (chorus, bridge, drop). The visual climax should align:

> The 8-second mark of the video should align with the bass drop in @audio1. The visual climax (the cluster detonating into the assortment) should hit on the drop. Slow-motion ramp begins 0.5 seconds before the drop, snaps back at the drop.

Audio peaks AND visual peaks aligned = production-grade impact.

---

## Held shots across phrase changes

Music videos breathe. After a fast cut sequence, hold a longer take across the phrase change.

> Cuts every 1 second across the verse (4 cuts). Held shot from 4 seconds to 8 seconds (across the chorus phrase change). Cuts resume at the bridge (every 0.5 seconds for 4 cuts). Held shot from 12 seconds to 15 seconds (across the outro).

The held takes give the eye a rest and let the music carry the moment.

---

## Beat-sync with VFX moments

Visual effects should land on beats:

> The VFX explosion at 8 seconds aligns with @audio1's bass drop. The shockwave ripple expands in time with the sub-bass tail (~1.5 seconds). The next cut (after the explosion) lands on the next downbeat of the chorus.

Audio + visual + VFX synchronized = layered impact.

---

## Limits

- Up to 3 audio references per generation
- Audio reference total duration ≤ 15s
- Cuts per generation ≤ 8 (so beat-sync at extreme BPM may require splitting)
- The model auto-aligns most cuts to audio if the audio reference is provided — explicit BPM is fallback when no reference

---

## Common beat-sync requests

- Music video with custom song
- Beat-aligned product montage (commercial montage to a track)
- Dance video synced to specific song
- Workout / fitness content beat-aligned
- Movie trailer-style edit synced to a track
- Recap / highlights edit synced to a song
- Multi-image animation cut to music

---

## Negative prompt

```
Negative: no off-beat cuts, no random cut intervals, no cuts that ignore @audio1's rhythm, no music change mid-video.
```

---

## Composition with `music-video` genre

Beat-sync is the capability that powers the music-video genre. They overlap heavily. Use beat-sync as the capability AND music-video as the genre when:
- The brief is explicitly a music video
- A song reference is the rhythmic anchor
- The visual style matches music video conventions (widescreen, dramatic lighting, vibrant grade)

Use beat-sync as a CAPABILITY only (without music-video genre) when:
- The brief is beat-aligned content but not a music video (a beat-aligned commercial, a beat-aligned explainer, a beat-aligned TikTok)
- The visual style is something other than music video (commercial product, UGC, explainer)
