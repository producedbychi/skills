# Produced by Chi skills

This is my personal collection of reusable AI skills and creative workflows for video, social content, and visual storytelling. Each skill has its own `SKILL.md`, plus any reference material, templates, or scripts it needs.

The skills use the standard `SKILL.md` format, so they can work with Codex, Claude, and other agents that support custom skills.

## What is included

- [Preproduction workflow](skills/preproduction-workflow/SKILL.md) is one skill with brief, treatment, AV script, breakdown, and paperwork modes. It can define a project from scratch, develop a creative direction, write a two-column audio and video script, plan shots and resources, and draft the business documents relevant to the project stage. Legal and tax terms need qualified review.
- [YouTube thumbnail generator](skills/youtube-thumbnail-generator/SKILL.md) creates, reviews, and improves YouTube thumbnails with a native image tool or a paste-ready prompt package.
- [Seedance video director](skills/seedance-video-director/SKILL.md) turns a video brief into a detailed Seedance 2.0 prompt. Its reference guides cover camera work, continuity, lighting, genre, and Seedance capabilities.

## How to use a skill

1. Open the skill you want inside `skills/`.
2. Copy the whole skill folder into your agent's custom-skills directory. Keep its `SKILL.md` and every supporting file together.
3. Start a new task and name the skill, or describe work that matches its purpose.

Install `preproduction-workflow` as one folder. Its modes live in `references/`, so there are no other skill dependencies. Ask for a creative brief, treatment, AV script, breakdown, specific project document, or the full workflow. The full workflow can begin with only a project idea; it marks unapproved choices as provisional and lists what is ready, pending, or not relevant. Supply approved company details and templates with the project when you need business documents. The public skill does not include private rates, payment details, or contract terms.

For example, install `skills/seedance-video-director/` as a complete folder. Do not copy only its `SKILL.md`, because it reads files in `references/` when it needs them.

## Repository layout

```text
skills/
  preproduction-workflow/
    SKILL.md
    references/
  youtube-thumbnail-generator/
    SKILL.md
  seedance-video-director/
    SKILL.md
    references/
```

## Adding a skill

Create `skills/<skill-name>/SKILL.md`. Place the skill's scripts, templates, and reference files in the same folder. Then add it to the list above.
