# Control locks

Six locks that decide whether a generation lands. Add the ones the diagnosis flagged. Each one is short — a sentence or two placed where it belongs in the block order, not a separate section.

---

## 1. First-frame occupancy lock

The single highest-value lock. Seedance's default instinct is to open on an empty or near-empty establishing frame and bring subjects in afterward, which wastes one to two seconds of a fifteen-second budget and breaks any prompt whose spatial read depends on seeing the relationship immediately.

When the shot must open with subjects present, say so directly:

> The first visible frame already contains both subjects in their locked positions. The spatial relationship is readable in frame one. No empty establishing frame, no delayed entry.

Allow an empty opening only when the user explicitly asks for one. If the user wants a fast establishing beat or a flash cut, it still has to carry the required subject or location information immediately — no empty flash cuts, no abstract filler, no unrequested landscape insert.

---

## 2. Spatial blocking lock

Define where everyone is before the camera gets described. For each subject that matters:

- screen position (left/center/right third, or x% when composition is asymmetric)
- depth layer (foreground / midground / background)
- distance from the landmark or from the other subject
- body facing direction
- gaze direction
- movement direction

**Weak spatial words and their replacements.** The words on the left let the model choose; the ones on the right do not.

| Weak | Strong |
|---|---|
| near the tree | boots planted inside the root circle |
| by the car | one hand flat on the scorched hood |
| beside her | shoulder within 20cm of hers, same depth plane |
| around the location | back against the north wall |
| somewhere in the yard | at the kerb edge, facing into the street |
| nearby | within 1 meter |
| next to the door | hand on the door handle |
| under the sign | standing directly beneath the sign, sign filling the upper third |

Worked example:

> The wounded figure stands within 1 meter of the burned-out car, right hand flat on the scorched hood. The other two stand together in the foreground, both facing him. The one in the field jacket holds screen-right of the pair, the one in goggles screen-left. Both torsos square to him, both gaze lines locked on him.

---

## 3. Gaze line and body orientation lock

Body direction and eye direction are separate channels. Seedance conflates them unless both are written.

Usable phrasing: *torso faces X* / *eyes stay locked on X* / *head turns toward X while the torso holds* / *back to camera* / *profile to screen-left* / *looks past the lens toward X*.

For dialogue: the speaking subject's lips move only for the scripted line. Other subjects listen with still lips. No off-screen voices unless the user asks for them.

---

## 4. Landmark proximity lock

If a subject must be near a specific thing, anchor with contact or a metric. This is the same discipline as spatial blocking, applied to the one relationship the shot is actually about — and it is worth stating twice in the prompt when the whole read depends on it (once in Frame Map, once in Movement).

Anchors that hold: *within 1 meter* · *touching* · *hand on the handle* · *back against the wall* · *boots inside the root circle* · *directly beneath the sign* · *in front of the rear passenger door* · *at the south kerb edge*.

---

## 5. Context isolation

Every prompt is a sealed document describing one shot. Nothing from the conversation, the script, or the previous generation belongs inside it. This matters most when working through a sequence in one session, which is when leakage is invisible and constant.

Strip before delivery:

- scene numbers, episode labels, script headers, slug lines
- previous-scene summaries
- subjects who do not appear in this shot
- reference tags not used in this shot
- props established earlier but not visible now
- subjects mentioned only in prior dialogue
- production notes not meant for the model
- the phrases: *same as before*, *previously*, *again*, *continues from*, *as above*, *from the last shot*, *the other character* without naming who
- platform and tool names (Seedance, Higgsfield, the model name)
- meta-commentary of any kind

The test: every tag in the prompt corresponds to a reference that is visible or required in this exact shot, and every noun in the prompt renders as a pixel.

---

## 6. Minimum-anchor character rule

The reference image is the source of truth for face, body, proportions, wardrobe, texture, and identity. Prose that re-describes what the reference already carries competes with the reference and degrades likeness.

Describe only:

- role or body type
- current state (what the body and face are physically doing)
- unique visible identifiers the reference cannot carry (damp hair, dirt on the cheek, torn sleeve, fresh bandage)
- action-critical body parts and props, with contact points
- voice character, only when there is dialogue

Leave out: full facial anatomy, wardrobe detail already visible in the reference, decorative adjectives, old injuries irrelevant to this shot, props not in use, relationship labels that do not change the frame.

Close each subject block with a lock-down line: *face, hair, wardrobe and silhouette identical to the reference across the full runtime.*

**Age-blind (hard rule).** Never describe a subject by age, in any form. Avoid: *boy, girl, child, kid, young, teen, little, junior, elderly, senior, 20yo, middle-aged.* Use role, build, and visible identity markers instead — "broad-shouldered figure in a blood-streaked hoodie," not "20yo male." This overrides any source system that puts age first in its character formula.

Formula:

> `@tag` — [role or build] + [current state] + [identifiers the reference can't carry] + [action-critical prop and contact point]. Face, hair, wardrobe and silhouette identical to the reference throughout.

Example:

> `@hero_ref` — broad-shouldered figure, tangled blond hair fallen across the eyes, blood-streaked grey hoodie, right shoulder roughly bandaged, left hand closed around a dented steel pipe at mid-shaft. Face, hair, wardrobe and silhouette identical to the reference throughout.
