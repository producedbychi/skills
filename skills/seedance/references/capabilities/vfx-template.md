# VFX / creative template replication

Reproduce creative transitions, ad templates, complex VFX, or cinematic moments from a reference video. The Seedance capability for "make me this exact ad / transition / VFX moment but with my elements swapped in."

---

## When the user is in this capability

- "This ad's transition is amazing — make me the same thing but with our product."
- "Reproduce this VFX template, swap in my character."
- "I want this exact creative — same beats, same effects, just with my brand."
- "Match this music video's VFX exactly, replace the artist with @image1."

If the user wants a near-1:1 reproduction of a reference video's creative template with element substitution, you're in VFX-template.

---

## Prompt structure

```
Reference @video1's [VFX / transition / creative template] + Replace [element in @video1] with @image[N] + [supplementary context]
```

Example:

> Reference @video1's full VFX sequence (the energy explosion, the shockwave rings, the particle dissolution). Replace the character in @video1 with @image1 (our hero), and the location with @image2 (a desert). Keep all VFX timing, all camera moves, all transitions identical to @video1. Only the character and location change.

---

## Critical distinction: VFX-template vs camera-replication

- **Camera-replication** = copy the camera grammar, leave the content fresh
- **VFX-template** = copy the creative TEMPLATE (camera + VFX + pacing + beats), substitute specific elements

VFX-template is the more aggressive replication. The result should look very similar to the reference video, just with different elements.

---

## What gets reproduced in VFX-template

- All camera moves
- All VFX (energy, particle effects, transitions, blooms)
- Pacing and cut rhythm
- Beat structure (the same beats happen in the same order)
- Color grade (often)
- Atmosphere (smoke, fog, debris)

What gets swapped:
- Character / subject identity
- Location / environment
- Specific products
- Color palette accents (sometimes)

---

## Tagging substitutions

Be explicit about which elements stay and which get swapped:

> @video1 is the template. Reproduce all camera moves, all VFX, all pacing, and all atmospheric effects EXACTLY.
>
> Substitutions:
> - Replace @video1's hero character with @image1 (our spokesperson).
> - Replace @video1's product with @image2 (our product).
> - Keep the location, color grade, lighting, and energy effects identical to @video1.

Without this explicit list, Seedance won't know which elements to keep vs swap.

---

## Common patterns

### Ad template reproduction
> Reference @video1's full ad creative. Reproduce the camera moves, transitions, and product reveal sequence. Replace @video1's product with @image1 (our brand's product). Keep all VFX, color grade, and pacing identical.

### Transition effect reproduction
> Reference @video1's transition effect (the chocolate-curtain-wipe at the 4-second mark). Reproduce this transition moment in my video at the cut between Scene 2 and Scene 3. Match the exact motion, color, and timing.

### VFX moment reproduction
> Reference @video1's transformation moment (the moment the character's body dissolves into geometric shards). Reproduce this exact VFX in my video, replacing the character with @image1.

### Cinematic moment reproduction
> Reference @video1's signature shot (the slow push-in across 8 seconds ending on the close-up). Reproduce this moment at the climax of my video. Replace the location with @image2.

---

## Limits

- Highly specific VFX may not transfer perfectly — Seedance approximates the effect vocabulary
- Branded creative (specific brand elements, logos, on-screen text) may bleed through unintentionally — use negative prompting to exclude
- Reference videos consume more credits than reference images
- 2–15 seconds reference video, 480p–720p, up to 3 videos per generation

---

## Negative prompting for VFX-template

Always include negative prompts for VFX-template to prevent bleed:

```
Negative: no @video1's text overlays, no @video1's logo elements, no @video1's brand colors that conflict with mine, no @video1's specific characters that aren't replaced.
```

This keeps the substitution clean.

---

## When VFX-template ISN'T appropriate

Don't use VFX-template when:
- The user wants creative inspiration but original output (use **camera-replication** for partial copy, **text-only** for fully original)
- The reference video is highly branded and the result needs to be distinct (legal / IP risk)
- The reference video is in a different genre / register and the brief calls for the user's own register

---

## Common VFX-template requests

- "Make this viral ad with our product instead"
- "Reproduce this music video moment with our artist"
- "Same magical transformation, our character"
- "This explosion shot, replace the building with our brand's element"
- "This anime fight intro template, our hero"
- "This product 360-degree spin reveal, our SKU"
