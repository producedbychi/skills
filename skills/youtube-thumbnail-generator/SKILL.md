---
name: youtube-thumbnail-generator
description: Create, refine, or brief YouTube thumbnails through an available native image tool or a paste-ready prompt package. Use for YouTube video covers and click-focused concepts, not generic images or video editing.
---

# YouTube thumbnail generator

Create a finished, truthful YouTube thumbnail that is clear in a crowded feed and in YouTube's TV interface. Choose a production route that fits the user's tools and preference.

## Choose a production route

Use the route the user names. If they have not chosen one, use an available native image tool. When no image tool is available, or when the user wants to work in another generator, deliver a prompt package instead of changing providers on their behalf.

- **ChatGPT native.** Use the host's `image_gen` tool when the user wants ChatGPT to render the thumbnail.
- **Google Antigravity.** Use Antigravity's native image-generation capability when the user works there. Antigravity currently uses Nano Banana 2 for generative-image tasks, but use the capability and model exposed in that environment rather than assuming a fixed model name.
- **Prompt package.** Give the user a ready-to-paste prompt, a reference-attachment plan, and a short review checklist. This route works with Gemini, Antigravity, ChatGPT, Claude, or another image generator.

When more than one native route is available and the choice will affect the result, ask which one the user wants. Clearly distinguish a rendered asset from a prompt package.

## Intake

Collect only details that materially affect the result. Use sensible defaults for the rest.

- Video topic, title, and intended viewer.
- The question the viewer should wonder and the feeling the image should create. Decide these before deciding what to depict.
- The main subject: a supplied face or character, an explicitly requested generated person, product, place, or graphic. Never introduce a person by default.
- Any face, character, product, logo, or source-frame references. Treat a reference thumbnail as style and composition direction, not an identity source.
- Aspect ratio. Default to 16:9.
- Exact headline text, if wanted, and the number of concepts or variants.
- Whether this is a standard long-form video, a Short, or a podcast. Default to long-form.

If the user does not give an exact count, render four genuinely different thumbnail concepts. A cleanup, resize, crop, or targeted edit does not count as a variant.

If a person is central but the user has not chosen who, ask once whether they want a supplied face, an explicitly generated person, or a people-free concept. When a face or character image is supplied, use it as a reference and require a recognizable identity match. Do not copy a reference thumbnail or invent a specific identity.

When the user supplies product photos, character assets, or a logo, use them as image references for every concept that depicts them. Check the result against those files before delivery. Do not replace a supplied product with a generic lookalike.

## Reference plan

Before rendering or writing a prompt, classify the supplied assets:

- **Must match:** a real person, character, product, logo, or outfit whose identity matters.
- **Look and pose:** a source frame, lighting reference, framing reference, or pose reference.
- **Atmosphere:** a location, palette, texture, or mood reference.

Make sure every must-match asset shown in a concept has a matching reference attached to that concept. Match the plan to the reference limit of the chosen image system. If the required must-match assets exceed that limit, say so and offer a prompt package, a staged composition plan, or a concept that covers the assets faithfully. Do not silently omit a requested product or substitute a generic version.

Create an attachment manifest in the same order that references are attached. Give every image its role and what must be preserved, for example: `Reference 1: girl identity, retain her face, hair, and hospital gown.` Use that mapping in the render prompt. Include the manifest in every prompt package so the user knows exactly which images to attach and why.

## Inspiration research

Use this optional mode when the user asks for inspiration, competitor research, or thumbnail trends. Gather 10 to 15 relevant references across the user's own successful videos when available, adjacent channels, the same video format, saved inspirations, and relevant non-YouTube visual media.

For each reference, identify the visual question, emotional pull, focal subject, title-and-thumbnail division of labor, composition, and what makes it readable at a glance. Use the findings to form original concepts. References guide the underlying idea and visual structure, not a copy of another creator's thumbnail.

## Concept and composition

Privately consider at least five directions. Then render the requested number of distinct directions, or four when no count was supplied. A good direction creates an information gap that the video honestly answers. It must read in under a second and have one obvious focal subject.

Decide how the title and thumbnail divide the information. The title may state the topic while the image supplies visual proof, a result, emotion, or an unanswered question. Use headline text when it adds a useful part of the promise. Honor exact user-supplied copy.

When the user has no visual direction, begin with the content type that best matches the video:

- **Tutorial or review:** make the result, tool, or decision visible so viewers see the benefit.
- **Challenge or experiment:** show the person, obstacle, scale, or stakes.
- **Personal story:** center the decisive emotional moment or a meaningful object from the story.
- **Transformation:** use a clear before-and-after contrast when both states are truthful and stay readable.
- **Explainer or analysis:** use one simple visual metaphor, object, or diagram that makes the idea concrete.
- **Product or collection:** make the real product the hero and use its supplied references.

Treat these as starting points. Change or combine them when the title, intended viewer, or supplied references call for a stronger direction.

Useful directions include a posed portrait, posed action, product as hero, before/after, versus, three-step progression, landscape, map or aerial view, graphical representation, repetition, size contrast, screenshot from the source video, text callout, and a plausible amplified version of one real story element. Combine directions only when the image stays simple.

Keep the main subject large, high-contrast, and separated from the background. Remove props and detail that do not strengthen the central idea. Use a split layout only when the user asks for a comparison, before/after, or panels. A scene containing two things is not automatically a split layout.

## TV-first 50% test

Design the thumbnail as though the bottom half may be hidden by YouTube's TV interface. Put the focal subject, hook, and any essential headline in the upper half, usually the top third. Before delivery, inspect the result as if its lower half were covered. The visible top half must still communicate the topic and create curiosity. If it fails, revise the composition before showing it.

Also inspect at a small feed-like size. The focal subject, emotion, and key visual element must still be obvious. Do not rely on the video title to create interest.

For a thumbnail rendered in the current host, complete this review manually before the user sees it. Inspect the full image, its 120px-wide feed-size appearance, and its visible upper half with the lower half treated as hidden. Do not generate or deliver a contact sheet for this check. If any view fails, make a targeted revision and repeat all three checks before presenting the thumbnail. For a prompt package, include the same three checks for the user to apply after rendering.

## Test and compare mode

When the user asks for a YouTube Test & Compare set, produce exactly three upload-ready thumbnails. Keep the video and core promise constant, then vary one major packaging choice per candidate, such as the focal subject, the visual question, or text-led versus visual-led presentation. State the hypothesis for each candidate.

Prepare each test image at 16:9 and at least 1280 x 720. YouTube runs concurrent thumbnail tests with up to three thumbnails and determines results by watch-time share, not click-through rate alone. A finished test can take days or up to two weeks. Treat an untested recommendation as a hypothesis, not a winner.

For standard concept exploration, keep the default of four genuinely different directions unless the user asks for another count.

## Learn from published results

When the user supplies a YouTube Analytics export or Test & Compare report, record the video title, the thumbnail variants, the test period, impressions, traffic source, and the reported result. Use YouTube's watch-time-share result for an official Test & Compare outcome. For an ordinary thumbnail swap, compare similar traffic sources over a meaningful period before deciding that a change helped.

Turn the result into one next hypothesis. Preserve the video's topic and viewer when comparing outcomes. A promising result on one video informs the next test, but does not become a universal template for every video.

## Text

Choose the amount of text according to the video's premise, the image's strength, and the intended viewing context. A short, truthful headline can make the premise clear at a glance. A text-free image can let a strong visual carry the hook.

When the video title or premise contains a strong short phrase, consider it as a headline candidate. For a comparison set, use text-led and visual-led directions when they create meaningfully different thumbnail options. For a single thumbnail, choose the approach that makes the hook clearest.

Use two to five words where possible. Put the headline in a clear upper-half area and make it high-contrast and readable at small sizes. Use user-supplied wording verbatim. Inspect every letter after rendering and correct an inaccurate text rendering with one targeted retry. Offer short headline options when the user asks for copy or testing.

Do not use real-platform logos, fake posts, fake reviews, or fake news graphics. Generic UI or labels are acceptable only when they accurately represent the video and the user asks for them.

## Generate and refine

For a native rendering route, use the selected image capability for each distinct concept or variant. Build a focused prompt that specifies the asset's use, topic, focal subject, style, composition, lighting or mood, palette, exact text when applicable, reference plan, and concrete constraints. Preserve user-provided detail instead of adding arbitrary story elements.

For a prompt package, provide:

- The one-sentence thumbnail premise and its division of labor with the title.
- The final prompt in a single paste-ready block.
- The attachments to add, grouped by must-match, look and pose, and atmosphere.
- The intended aspect ratio, focal-subject placement, headline text if any, and a small-size review checklist.

Use the chosen image system's existing edit capability for an edit. State the invariants clearly. Make one targeted change at a time, such as expression, background, color, headline placement, or removal of clutter. Preserve identity, pose, clothing, logo, and composition unless the user asked to change them.

For long-form videos, deliver a 16:9 JPG or PNG at the highest practical resolution. Keep every Test & Compare candidate at least 1280 x 720. Shorts and podcast thumbnails need their own aspect-ratio route rather than a recycled 16:9 layout.

## Review before delivery

Check every result for:

- Accurate and recognizable supplied identities or products.
- A single readable focal subject and no distracting clutter.
- A truthful relationship to the video topic.
- Clear emotion or intrigue without relying on the title.
- The TV-first 50% test and small-size readability.
- Correct text, if used, and no stray words, watermark, or unintended brand marks.
- The chosen route's reference plan. Every required person, product, logo, and character must be present and recognizable.

Retry a failed render at most twice. If it still misses a requirement, report the issue instead of presenting it as final.

For a comparison set, review every concept against the same criteria and present all viable candidates. Give a recommendation, but do not claim one "won" unless it was compared with other creative concepts or measured in a real A/B test. If the user asks for a single final file without choosing, select the strongest reviewed concept and state why.

