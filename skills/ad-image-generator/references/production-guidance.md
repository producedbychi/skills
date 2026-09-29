# Production guidance for static ads

Use the section that matches the available tool. Check that tool's current instructions for reference limits, supported sizes, editing behavior, costs, and output files. These details differ by provider and can change. Do not claim a model can preserve an asset exactly because a prompt asked it to.

## Image generator with reference images

Inspect each supplied asset before use. Assign it a role: exact product or package, exact brand mark, person identity, style reference, or loose scene reference. List those roles in the prompt or tool call. A style reference does not authorize copying a competitor's ad.

Ask the generator to create only what may change. Keep exact logos, packaging, interface screens, footage stills, and regulated copy as supplied pixels when the tool supports that. If the tool cannot reliably lock them, render a background or scene with room for those elements, then composite the originals in an editor. Do not describe a generated approximation as an exact match.

Avoid plausible but false detail. Generated package backs, ingredient lists, dashboard numbers, customer quotes, awards, and third-party marks can become unsupported claims. Keep unverified surfaces out of view or replace them with approved assets.

If exact text matters, use a text-free base image and typeset it separately unless the selected generator has proved reliable for that specific text. Inspect every word after rendering. Give the model room for the final type and keep faces and product details away from likely crop edges.

## Editing or compositing tool

Use the original file for any element whose identity must match. Match its perspective, contact shadow, lighting, and scale to the scene without repainting its label or logo. Preserve the brand's actual type and color values when supplied. Export each requested placement deliberately; stretching one finished layout to a different aspect ratio is not an adaptation.

## Prompt-only handoff

Provide one paste-ready prompt for the generated portion and a separate placement plan for exact product, logo, and text assets. Name each required attachment in order. Mark any file that has only been described, not inspected. State which text belongs in the image and which belongs in platform fields. Include the intended crop and a short finish checklist so the user can tell whether the generated result is usable.

## When a render fails

Identify the failing element before retrying. A composition or crop problem may justify a focused edit. Repeated text or identity drift calls for compositing the exact asset rather than another full regeneration. Recheck the repaired image at full size and feed size. If the available tool still cannot deliver an accurate file, report the specific defect and provide the usable base image or prompt package.
