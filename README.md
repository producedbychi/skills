# My skills

This is my personal collection of reusable agent skills. Each skill has its own `SKILL.md`, plus any reference material, templates, or scripts it needs.

The skills use the standard `SKILL.md` format, so they can work with Codex, Claude, and other agents that support custom skills.

## What is included

- [YouTube thumbnail generator](skills/youtube-thumbnail-generator/SKILL.md) creates, reviews, and improves YouTube thumbnails with a native image tool or a paste-ready prompt package.
- [Seedance](skills/seedance/SKILL.md) turns a video brief into a detailed Seedance 2.0 prompt. Its reference guides cover camera work, continuity, lighting, genre, and Seedance capabilities.

## How to use a skill

1. Open the skill you want inside `skills/`.
2. Copy the whole skill folder into your agent's custom-skills directory. Keep its `SKILL.md` and every supporting file together.
3. Start a new task and name the skill, or describe work that matches its purpose.

For example, install `skills/seedance/` as a complete folder. Do not copy only its `SKILL.md`, because it reads files in `references/` when it needs them.

## Repository layout

```text
skills/
  youtube-thumbnail-generator/
    SKILL.md
  seedance/
    SKILL.md
    references/
```

## Adding a skill

Create `skills/<skill-name>/SKILL.md`. Place the skill's scripts, templates, and reference files in the same folder. Then add it to the list above.
