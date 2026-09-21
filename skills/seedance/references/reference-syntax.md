# Reference syntax — semantic tags

How to handle reference materials (images, videos, audio) inside Seedance prompts.

---

## Semantic tags are the default

Use descriptive tag names the user supplies, not index numbers.

- Lowercase, underscore-separated, named for what the element *is*: `@sol_ref`, `@berlin_bunker_plate`, `@white_camaro`, `@rain_plate`, `@stadium_wide`
- Character references take a `_ref` suffix. Environment plates take `_plate`. Objects, vehicles and props take a descriptive noun.
- Prefixed with `@` inside the prompt body

Semantic tags survive re-ordering, survive a re-upload in a different slot, and stay readable when a prompt is revisited a week later. Index tags do none of those things.

**Never invent tag names on the user's behalf.** If the references for this scene are not yet named, ask for the tag list before writing. Once tags are locked in a session, carry them forward — the user will not re-name the same character reference on every prompt.

**Index fallback.** Some frontends require positional references. When the user's pipeline needs them, `@image1`–`@image9`, `@video1`–`@video3`, `@audio1`–`@audio3` work, as does `<<<image_1>>>` on some frontends. Seedance's native syntax is `@图片1` / `@视频1` / `@音频1`; the English forms work identically on most frontends. **Be consistent within a single prompt** — mixing `@image1` and `<<<image_1>>>` makes Seedance treat them as different references.

---

## Canonical-over-plate rule

Every named subject that appears in a scene gets its own canonical reference tag, even when that subject is also visible in the rendered environment plate. Characters, vehicles, props, creatures.

The plate carries the world — location, weather, light, set dressing. Canonical references carry identity — face, body, livery, markings, silhouette. Subject Locks anchor to canonical tags; the World Plate anchors to the plate tag. No exceptions, even when a subject reads clearly in the plate.

---

## Reference limits per generation

- **Up to 9 images**
- **Up to 3 videos**
- **Up to 3 audio files**
- **12 max combined** across all reference types

If a scene needs more than these limits allow, split into multiple generations and chain in the NLE. This skill produces independent segment prompts with continuity rules between them.

---

## Always tag the reference's role

The most common cause of reference confusion is unstated role. When you mention a tag in a prompt, immediately tell Seedance what role it plays.

### Image roles

- **First frame.** Seedance starts the video on this exact composition. Tag: "`@kitchen_plate` as first frame"
- **Last frame.** Seedance ends the video on this composition. Tag: "`@final_pose` as last frame"
- **Character reference.** A character in the video should look like the person in the image. Tag: "the figure matches `@sol_ref`"
- **Scene background reference.** The environment should look like the location in the image. Tag: "the alley geography and materials follow `@alley_plate`"
- **Style reference.** The whole video should adopt the visual style of the image (color, lighting, aesthetic). Tag: "cel-shaded aesthetic follows `@style_ref`"
- **Product reference.** A specific product should appear identically. Tag: "the product is `@tumbler_ref`, exact form held"
- **Wardrobe reference.** A specific outfit should be replicated. Tag: "wardrobe follows `@buyer_ref`"

### Video roles

- **Camera moves reference.** Copy the camera motion vocabulary. Tag: "camera grammar follows `@dolly_ref`"
- **Action choreography.** Copy specific action beats. Tag: "fight choreography follows `@fight_ref`"
- **VFX template.** Copy specific visual effects. Tag: "reproduce the transition from `@vfx_ref`"
- **Pacing / rhythm reference.** Copy the cut cadence or beat rhythm. Tag: "edit pacing follows `@pace_ref`"
- **Tone / mood reference.** Copy the emotional register. Tag: "tonal reference `@tone_ref`"

### Audio roles

- **Background music.** Tag: "bed references `@track_ref`"
- **Voice / narration tone.** Tag: "narrator tone references `@vo_ref`"
- **Sound effects.** Tag: "impact texture references `@impact_ref`"

---

## Multiple roles per reference

A single reference can serve multiple roles. State each one.

Example: "`@buyer_ref` as first frame, the figure throughout is `@buyer_ref`, wardrobe follows `@buyer_ref`."

Don't make Seedance guess which role applies in which beat. Be explicit each time.

---

## Tag hygiene across a session

**Every tag in the prompt must be used in this shot.** A tag carried over from the previous prompt is the most common form of context leakage — the model renders a subject who should not be in the frame. Run the context isolation pass in `control-locks.md` before delivery.

**Multi-version prompts.** When producing two or three versions of a prompt, shared references keep the same tag across versions. Version-specific references get their own distinct tags (`@first_frame_a`, `@first_frame_b`) — never reuse one tag for different files across versions.

**Tell the user what to upload.** List each tag with what file goes in that slot. With semantic tags the mapping is self-documenting, but state it anyway when there are more than three references.

---

## When to use first frame / last frame control

Seedance supports setting both a starting frame AND an ending frame as separate reference images. The model generates the arc between them.

**Use first frame only when:**
- You need precise control over the opening composition
- You're chaining segments and the start needs to match the previous segment's end
- The opening is the dramatic anchor of the scene

**Use first frame + last frame both when:**
- The video is a transformation arc (state A → state B)
- The emotional read depends on the starting and ending compositions matching specific images
- You want Seedance to generate the entire transition without drift

**Don't use last frame when:**
- The ending should be Seedance's emergent surprise
- The video is action-forward and constraining the ending kills the kinetic energy
- You don't have a strong vision for the ending composition

---

## Reference image generation prompts

When the user's request needs reference images they don't yet have, this skill produces both:

1. The Seedance video prompt (using the references by their tags)
2. The GPT Image 2 prompts for each reference

Match the reference image style to the video subject:

- **Product / commercial** → editorial product photography, clean studio, soft directional light
- **Action / cinematic** → cinematic still photography, ARRI ALEXA aesthetic
- **Anime / animation** → matching anime art style (cel-shaded, ghibli, etc.)
- **Xianxia / fantasy** → 3D Chinese animation rendering, concept art
- **Sci-fi / cyberpunk** → futuristic concept art, neon-rendered CG
- **Documentary / heritage** → realistic photography with period accuracy
- **UGC / authentic** → smartphone-style photography, natural light, imperfection
- **Horror / thriller** → atmospheric photography, deep shadows, tension
- **Music video** → high-contrast editorial photography, stylized

The reference image prompt should be detailed (4–8 sentences) covering subject, environment, materiality, lens choice, color grade, and finish. Same level of specificity as the video prompts themselves.

---

## When references are NOT provided

If the user's request implies reference materials that haven't been attached:

1. Ask which references they have ready (especially for character / product consistency)
2. If they don't have them, produce the GPT Image 2 prompts for the references they need, alongside the Seedance video prompt
3. Note in the output which references must be generated first

Example output structure when references need to be generated:

```
**Required references (generate first):**
- @image1 — the buyer character at three emotional states (neutral, frustrated, relieved)
  - GPT Image 2 prompt: [...]
- @image2 — the dark chocolate cluster on warm-stained oak
  - GPT Image 2 prompt: [...]

**Seedance video prompt (use after references are generated):**
[the prompt with @image1 and @image2 tagged in their roles]
```

---

## Special platform notes

- The official ByteDance / Jimeng Seedance frontend blocks uploaded images / videos containing realistic human faces. Other Seedance frontends (Higgsfield and similar) don't enforce this. If the user's pipeline is the official ByteDance frontend, flag the constraint when the request involves human faces. If they're on another frontend, no constraint.
- Reference videos consume more credits than reference images on most Seedance pricing tiers. Mention this when a request would use a video reference but an image reference would do the job equally well.
- Image input formats: jpeg / png / webp / bmp / tiff / gif, each <30MB
- Video input formats: mp4 / mov, each <50MB, 480p–720p, total duration 2–15s across all video references
- Audio input formats: mp3 / wav, each <15MB, total duration ≤15s across all audio references
