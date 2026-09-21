# Sound control

Direct dialogue, voice tone, and sound effects in the prompt. Seedance generates audio natively — this capability gives you control over what it generates.

---

## When the user is in this capability

- "I want narration over this scene with a specific voice tone."
- "Match the voice texture from this audio reference."
- "Add specific sound effects — door slam, breath, glass breaking."
- "The character should speak this exact dialogue."
- "Use @audio1 as the voice reference for the narrator."

If the brief has audio direction (dialogue lines, voice tone, specific SFX), you're in sound-control.

---

## Prompt structure

```
[Picture description] + [Voice / narration tone reference @audio[N]] + [Dialogue lines in quotes] + [SFX direction]
```

---

## Dialogue formatting

Dialogue lines go in quotes. The speaker and emotional register goes in parentheses before the line.

> Picture (0–5s): The buyer at her desk, expression frustrated.
> Line (Buyer, exhausted): "I can't keep doing this."
> Picture (5–10s): The Hayden Valley case opens, the assortment revealed.
> Line (Buyer, dawning relief): "...wait."

The `(Speaker, emotion)` tag tells Seedance the performance register. Don't write the emotion as a separate sentence — bake it into the line tag.

---

## Voice tone reference

When the user provides a voice reference (`@audio1`):

> Narrator voice tone references @audio1. The narrator should match @audio1's timbre, cadence, and emotional register.

If using a video reference for voice (the original Seedance "video reference for voice" pattern):

> Narrator voice tone follows @video1 (use the speaker's voice from this video as the audio reference).

---

## SFX direction

The SFX block lives at the end of the prompt:

```
SFX: [time-aligned sound effects matching the picture beats]
```

Example:

```
SFX: 0–5s ambient office tone with distant phone ringing, single sigh from the buyer, paper rustle as she shifts the spreadsheet; 5–10s soft thud as the case lands on the desk, single beat of silence as she pauses, soft kraft-paper rustle as the flaps unfold; 10–15s warm room tone hum, the buyer's breath releasing slowly, single satisfied "...okay" beneath the breath.
```

Time-aligned SFX matches each picture beat. Even though Seedance generates the audio natively, the SFX block guides the energy.

---

## Music direction

For background music (BGM):

> Background music: warm cinematic underscore, single-piano-and-strings, builds slowly across the full duration, swells at the 10-second mark, settles into resolution at the close.

Or with a music reference:

> Background music references @audio1's mood and tempo. Match the rhythm and emotional register.

---

## Negative prompts for audio

Audio negative prompts:

```
Negative audio: no background music (silent except for SFX), no narration unless explicitly specified, no spoken dialogue (silent scene), no inappropriate accent shifts, no voice mismatches between beats.
```

For "silent scene" requests:

```
Negative audio: NO MUSIC, NO SFX, NO DIALOGUE — pure silence with only ambient room tone.
```

---

## Common sound-control requests

- "Generate this commercial with this exact voiceover."
- "Add narration that sounds like David Attenborough."
- "Match the voice from @audio1 — cloning a specific actor's tone."
- "Silent scene with only ambient room tone, no music."
- "Action scene with specific SFX — gunfire at 3s, glass breaking at 5s, slow-motion stretch at 7s."
- "Music video synced to @audio1 — cuts on the beat."

---

## Limits

- Up to 3 audio references per generation
- Audio reference total duration ≤ 15s
- Each audio file < 15MB
- Voice cloning works best when the audio reference is clean (no background noise)
- Specific celebrity voice cloning may be blocked by Seedance's content policy — use generic voice descriptions when in doubt

---

## Dialogue language preservation

When dialogue is provided in a specific language, preserve it. Don't translate user-provided dialogue.

If the user provides dialogue in Mandarin, the prompt's dialogue lines stay in Mandarin. The picture descriptions can be in English; the spoken lines stay native.

> Picture (0–5s): The merchant raises both hands in protest.
> Line (Merchant, defensive): "我没有偷你的羊！" (I didn't steal your sheep!)
> Picture (5–10s): The accuser steps forward, knife drawn.

---

## SFX vocabulary by genre

Different genres call for different SFX vocabulary:

### Action
- Impact thuds (shudder, slam, crash)
- Breath punches (recoil, exertion)
- Mechanical sounds (gun click, blade unsheathing)
- Slow-motion stretched audio (RAMPS TO SLOW MOTION as bullet drifts)
- Snap-back beat (SNAPS BACK to real-time on impact)

### Cinematic / drama
- Ambient room tone, weather, environment
- Single instruments under dialogue
- Held silences before key lines
- Soft physical sounds (cup setting on table, fabric rustle)

### Horror
- Low-frequency rumbles, environmental dread
- Sudden silence (NO AMBIENT) at threat reveal
- High-frequency tinnitus tones
- Wet drips, distant creaks, single sharp impacts

### Commercial / explainer
- Clean ambient, no competing noise
- Functional sounds (button click, lid pop)
- Soft music underscore
- Clean voice room

### Music video
- Music IS the foreground
- Footstep impacts double the kick drum
- Cuts hit on beats
- Minimal SFX competition

---

## Audio + visual sync

When audio drives visual (music videos, dialogue scenes):

> Cuts in the picture should land on the audio beats. The first cut at 0–0.5s, second cut at 1.0s, third cut at 1.5s — matching the kick drum pattern of @audio1.

Or for dialogue-driven cuts:

> Cuts happen on dialogue beats — at the start of each line. The reaction cut happens at 0.5s after the line ends.

State the sync explicitly. Don't leave audio-visual alignment to Seedance's interpretation.
