# Consistency control

Maintain character / product / scene consistency across shots using reference images. The Seedance capability for "this person should look like @image1 across all shots" or "this product should appear identically in every frame."

---

## When the user is in this capability

- "I want the same character to appear in 5 scenes."
- "The product needs to look identical across all shots."
- "Here's the buyer's character sheet, use them in scenes 1 and 6."
- "I have @image1 for the hero and @image2 for the location."

Whenever the brief requires the same identity / form to persist across visual moments, you're in consistency control.

---

## Prompt structure

```
[Character] @image[N] + [action / story] + [scene] @image[N] + [camera / lighting]
```

The reference images appear inline at the points of identity.

Example:

> The buyer @image1 walks through a clean fulfillment warehouse @image2, hands clasped behind her back. She passes shelves of identical Hayden Valley bulk cases. Camera tracks her laterally at chest height. Warm Golden Hour grade.

The `@image1` tags the buyer's identity. The `@image2` tags the location. Seedance maintains both across the generation.

---

## What references can anchor

- **Character** — face, body, clothing, hair, identifiable features
- **Product** — exact product form, color, packaging
- **Wardrobe** — specific outfit (slate-blue button-down, charcoal lanyard)
- **Scene / environment** — location, background, props
- **Style** — the visual aesthetic of the reference image (cel-shaded, 3D realistic, vintage film)

Each reference can do one or several of these — state explicitly what role it plays.

---

## Tagging the reference role

Always state what the reference is for:

- "The buyer matches @image1's slate-blue button-down and charcoal lanyard."
- "The cluster matches @image2's exact form factor."
- "The warehouse interior resembles @image3."
- "Visual style follows @image4 (cel-shaded anime aesthetic)."

Without role tagging, Seedance may copy the wrong elements (the lighting from a character reference, the framing from a style reference).

---

## Multi-reference patterns

When multiple references are in play, list them at the top of the prompt:

> @image1 — the buyer character (use for identity, wardrobe, hair)
> @image2 — the warehouse interior (use for location, lighting, scale)
> @image3 — the Hayden Valley bulk case product (use for exact product form)

Then reference them inline as the prompt proceeds:

> The buyer @image1 walks through the warehouse @image2, eyes scanning the rows of bulk cases. She stops in front of one, lifts the case @image3 off the shelf, sets it down on a nearby pallet. The case face is held clean for label composite.

---

## Style-only references

When an image is a STYLE reference but NOT a CHARACTER reference, clarify explicitly:

> @image2 is the visual style reference ONLY — use this image for lighting, color palette, environment design, and 3D claymation aesthetic. DO NOT use the character from @image2. Create a NEW original character in the same claymation style: [describe the new character].

Without this clarification, Seedance will copy the character from @image2 along with the style — and you'll get a wrong character in your scene.

---

## Character + product simultaneous consistency

For commercial work where both character and product appear across shots:

> @image1 — buyer character (identity, wardrobe)
> @image2 — Hayden Valley assortment composition (product breadth)
>
> The buyer @image1 sits at her desk in front of an open Hayden Valley case revealing the assortment from @image2. She lifts a single dark chocolate cluster from the case, examines it, sets it back. Camera medium close-up at 50mm.

Both references stay anchored across the generation.

---

## Limits on consistency

Seedance maintains identity well across 4–6 cuts inside a single 15s generation. Past 6 cuts:

- Identity may drift (slight feature shifts)
- Wardrobe may drift (sleeve roll changes, lanyard moves)
- Hair may drift (parting changes, length shifts)

For projects requiring consistency across MORE than 6 cuts in 15s, split into multiple generations and use the same reference images in each. The references hold consistency across separate Seedance calls.

For projects requiring consistency across multiple SCENES (each its own generation, like Hayden Valley's 11 scenes), the references are the consistency mechanism. Generate each scene with the same character / product references and Seedance will maintain identity across scenes.

---

## Reference image generation

When the user needs reference images they don't have, generate the GPT Image 2 prompts for them. See `references/genres/<genre>.md` for style suggestions per register.

The reference image prompt should produce an image suitable for Seedance to use:
- Subject is clearly visible and centered
- No watermarks or text overlays on the image
- Consistent lighting that's appropriate to the video's lighting register
- Resolution sufficient for Seedance to read details (higher resolution is better)
- Single subject per image (don't put two characters in one reference unless they always appear together)

For character consistency: produce a "character reference sheet" with multiple poses on a clean studio backdrop. This gives the Seedance pipeline a clean isolated subject.

For product consistency: produce a clean editorial product photo against a controlled background.

For environment / scene consistency: produce a still photograph of the location.

---

## When consistency is partial

Sometimes the user wants the CHARACTER to be consistent but the ENVIRONMENT to change:

> The buyer @image1 in three different settings: 0–5s in a cluttered warehouse office, 5–10s in a fulfillment dock, 10–15s in her clean modern office. The character identity holds across all three; the environments are distinct.

In this case, only @image1 is referenced for consistency. The environments are generated fresh from text descriptions.

---

## When consistency conflicts with action

Heavy action can degrade Seedance's consistency mechanism. If the brief calls for both:
- "She fights three opponents simultaneously, taking heavy damage" (heavy action)
- "She maintains the same face / hair / wardrobe throughout" (consistency)

Seedance may prioritize the action and drift on the identity. Mitigate by:
- Limiting the action to 2–3 distinct beats
- Reasserting the identity reference at each beat ("she @image1 lands the strike, she @image1 dodges the counter, she @image1 sets up for the finishing move")
- Keeping wardrobe / hair language explicit at each beat

---

## Common consistency-control requests

- Brand spokesperson appearing across a multi-scene ad
- Product hero appearing identically across multiple scenes
- Recurring character in episodic content
- Founder / talent recurring across documentary segments
- Character moving through multiple environments (the buyer in commercial Scene 1 and Scene 6)
- Product in different lighting / contexts (showroom, in-use, in-context)
