# Seedance 2.0 — Engine rules

These are hard rendering constraints of the Seedance 2.0 engine. Violating them produces broken output — characters teleporting, action that doesn't render, off-screen events that the model can't represent. They apply universally regardless of capability, format, or genre.

---

## Action beats = intent + named technique, not biomechanics

Seedance renders compressed intent better than joint-by-joint mechanics.

✅ "Spinning back kick connects, rib cage buckles."
❌ "Left forearm rotates 45° to deflect the incoming right hook at wrist level."

If the user names a specific move (a haymaker, a chokehold, a roundhouse, a shoulder check), preserve it. If the user describes joint mechanics, compress to the move's name or its intent.

---

## Describe force and direction, not destruction sequence

The engine handles the destruction physics if you give it the impact direction.

✅ "Driven into the car, metal buckling, glass spider-webbing."
❌ "Thrown into side door, glass shatters, uses rebound to sweep leg into the side panel."

---

## Spatial continuity breaks on cuts

After any cut, re-anchor the scene: who is where, which direction they face, what they're holding. Without re-anchoring, Seedance will renegotiate spatial relationships and characters will drift.

If a character moves left-to-right before the cut, state that direction explicitly after the cut.

---

## ≤ 3 characters tracked across cuts

Seedance cleanly tracks up to three characters across cut boundaries. Past three, identity bleeds. If your scene has more than three (a crowd, an arena, a wedding), name the **acting pair** plus an interaction vector per shot. Treat the rest as environment.

---

## Exit-frame = implicit cut

When a character leaves the frame, they're gone for the remainder of that shot. Never choreograph exit + re-entry in the same continuous shot — Seedance will either drop the re-entry or create a duplicate character.

If you need a character to leave and return, that's two shots with a cut between them.

---

## Off-screen = nonexistent

Whatever the camera doesn't see in the current shot, the model has no representation of. State changes must be shown on camera before being referenced.

❌ "She walks past the dead body in the hall." (the body wasn't established on camera)
✅ "She walks past the body slumped against the wall, shoes pointing toward the door." (the body is in the current shot)

If the user's scene needs an off-screen state change to drive a beat, show that state change in a previous shot.

---

## Avoid reflection shots

Seedance breaks scene geometry when rendering reflections in blades, puddles, mirrors, glass surfaces. The reflected world doesn't match the actual world — character positions flip, environments don't track, lighting goes off.

If you need a reflection beat for narrative reasons, frame it so the reflection is a small portion of the shot rather than the focal subject. Macro detail of an eye reflecting flame works. A full reverse-via-mirror does not.

---

## Only describe what can be seen or heard

The engine cannot render abstract concepts, smells, internal thoughts, off-screen events, or things the camera doesn't see in the current shot. Translate everything to physical observable behavior.

❌ "The air smells of pine."
✅ "Pine needles covering the ground, wind moving through branches."

❌ "She feels nervous."
✅ "Her thumb taps the side of her glass, eyes scanning the room left to right."

❌ "He's been doing this his whole life."
✅ "His grip on the tool is automatic, no glance down."

---

## Micro-expressions work when described as physics

Faces render well when you describe the muscle-level transformation. They render flat when you label the emotion.

✅ "Jaw clenches, nostrils flare, eyes hold."
✅ "Brow softens, corners of the mouth lift, breath releases through the nose."
❌ "Looks angry."
❌ "Feels relieved."

This is the most common upgrade for prompts that feel like still life. Convert every emotion label to its physical signature.

---

## Generation duration limits

- Hard cap: 15 seconds per generation
- Sweet spot: 4–15 seconds
- Below 4 seconds the engine has too little time to execute a scene
- 4–8s: single action / single product moment / short reveal — no timestamp breakdown needed
- 9–12s: complete short scene — optional 2–3 stage timestamps
- 13–15s: complete narrative — strongly recommend 3–4 stage timestamps

For requests >15s, output independent segment prompts with continuity rules between them. Don't try to fit a longer narrative into a single 15s call — the engine will compress badly.

---

## Aspect ratio

Default 16:9 unless the user says otherwise. Common alternatives:
- `9:16` — vertical / mobile / TikTok / Reels / Shorts
- `1:1` — square / Instagram feed
- `2.35:1` — cinematic widescreen / film letterbox
- `4:5` — Instagram portrait

State the aspect ratio in the spec footer, which sits OUTSIDE the prompt code block ("Total: 15s / 6 shots / 16:9"). Inside the prompt body it competes with the Camera Capture line.

---

## Reference material limits

- Up to 9 images per generation
- Up to 3 videos per generation
- Up to 3 audio files per generation
- 12 max combined across all reference types

If the user's scene needs more references than these limits allow, split the scene into multiple generations and chain in the NLE.

---

## What the engine generates natively

- Sound effects and music — Seedance generates audio natively. You can direct it via SFX blocks and audio reference tags.
- Auto-storyboarding — if you don't specify shot structure, Seedance plans shots from the prose. This is fine for short single-action prompts. Past 8 seconds, specify shots explicitly so you keep control.
- Auto-camera moves — if you don't specify camera, Seedance picks based on the action verbs. Specify camera explicitly when you care about the read.

---

## Resolution

Seedance outputs up to 2K. Specify "high resolution" or "2K output" inside the Camera Capture line if your downstream pipeline needs it. The engine doesn't always default to maximum without the cue.

---

## Specific motion content for body parts (production-tested)

When a hand, face, or body part moves, specify EXACTLY what motion it's performing. State language describing what something IS produces random motion when Seedance interprets the prompt. Verb-direction language describing what something DOES produces deliberate motion.

❌ "The hand TIGHTENS on the pen." (state — Seedance generates random hand motion to interpret "tightens")
✅ "The hand draws a hard X across the spreadsheet line item in three rapid diagonal strokes — first stroke down-and-right, second up-and-right crossing the first, third retraces the first to reinforce it. The pen leaves wet glossy ink visible on the paper."

❌ "Knuckles drawn." (state)
✅ "Knuckles whitening as the grip tightens, the index finger curling tighter against the pen barrel."

The rule is: every body-part beat must answer the question "what is the body part DOING in this beat?" with a specific verb-driven action. If the answer is "holding still while looking tense" — write the holding-still and the visible-tension as separate concrete behaviors (jaw set, gaze locked, breath held). Never leave the motion implied.

When a hand is shown writing, drawing, signing, or marking, specify what mark it makes (a circle, an X, a strikethrough, a specific letter or word) AND that the writing instrument leaves visible material on the surface (ink, pencil, marker streak). Without these, Seedance generates a hand moving over a page with no marks.

---

## Audio-visual sync for body sounds (production-tested)

Body sounds in the SFX block require corresponding visible body motion in the prompt. The engine renders visuals from the prompt body, audio from the SFX block — they read independently unless explicitly linked.

❌ Prompt: "shoulders carry a faint slump" + SFX: "single soft exhale through the nose"
(Result: Seedance renders the shoulders correctly and ignores the audio cue. The actor doesn't open their mouth or visibly exhale.)

✅ Prompt: "At 2.3 seconds the buyer's MOUTH PARTS, lips opening into a soft O shape. A long visible exhale RELEASES through the open mouth, jaw shifting downward with the breath, chest visibly falling." + SFX: "audible visible exhale through the buyer's open mouth at 2.3s"

The list of body sounds that need visible motion:
- **Sigh / exhale:** mouth parts, lips form O shape, jaw shifts downward, chest falls
- **Inhale / gasp:** chest rises sharply, eyes widen, lips part
- **Sniff:** nose wrinkles, brief upward head motion
- **Gulp / swallow:** throat moves visibly, jaw shifts
- **Yawn:** jaw drops fully, head tips back
- **Cough / laugh / cry:** chest convulses, mouth shape changes per the sound

When the scene is POV (no body visible to perform the sound), DO NOT include body sounds in the SFX block. Use environmental sound only (room tone, distant ambient, object sounds the visible body parts can plausibly make — fingertip taps, fabric rustle, cup-on-wood).

---

## Sub-second cuts require dedicated reference images (production-tested)

Seedance reliably renders one cut per reference image inside a single generation. If a prompt describes three sub-second cuts but only provides two reference images, Seedance renders two cuts and merges or skips the third. The "extra" cut described in the prompt does not appear in the output.

For high-density cut sequences (three or more cuts in under 4 seconds), one of three approaches:

**Option A — Provide one reference image per cut.** A 3-cut macro sequence needs 3 distinct reference images for the 3 subjects. This is the most reliable.

**Option B — Extend the duration so each cut has at least 1 second.** Two cuts at 1.5s each renders better than four cuts at 0.5s each. The action language can compensate for fewer cuts.

**Option C — Render each cut as its own Seedance generation and assemble in the NLE.** Each generation gets a single subject and full creative attention. The cuts come from editing, not from a single multi-cut generation.

The trap to avoid: writing four sub-second cuts in a single prompt with only two reference images and assuming Seedance will create the missing two. It won't. It will merge or skip.

---

## Action intensity must match the action register

When the genre composition includes action-intense, the action prose must read as EXTREME. Tier 4 verbs without intensity modifiers can still render as subtle — words like "lifting" and "cascading" describe motion but don't push it into kinetic-cinematic territory.

The fix is two-part:

**First — push the verb to Tier 4 / Tier 5.** Replace "LIFTING" with "DRIVES upward and RIPS clear." Replace "CASCADING" with "ERUPTS outward in a violent wave."

**Second — add intensity modifiers.** Words like "violently," "explosively," "in a dramatic burst," "with extreme force," "as if struck by something invisible." These tell Seedance the motion is cinematic-extreme not domestic-subtle.

Words to BAN inside action-intense beats: imperceptibly, subtly, gently, softly, quietly, lightly, faintly, almost, barely, slightly. These words signal restraint and Seedance generates restrained motion.

The action-intense product motion test: would you describe this motion the same way if you were directing a Marvel film? If yes, the intensity language is calibrated. If no, push harder.
