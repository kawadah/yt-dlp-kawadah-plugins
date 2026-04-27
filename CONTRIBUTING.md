# CONTRIBUTING

Refer to these yt-dlp docs when developing:

- [Plugin Development wiki](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development) — plugin structure and registration
- [CONTRIBUTING.md](https://github.com/yt-dlp/yt-dlp/blob/master/CONTRIBUTING.md) — extractor coding requirements and best practices (use of `traverse_obj`, `url_or_none`, etc.)
- [extractor/common.py](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/extractor/common.py) — available info dict fields and helper methods
- [utils/_utils.py](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/utils/_utils.py) — utility functions (`unified_timestamp`, `url_or_none`, `int_or_none`, etc.)
- [utils/traversal.py](https://github.com/yt-dlp/yt-dlp/blob/master/yt_dlp/utils/traversal.py) — `traverse_obj` and related traversal utilities

## Getting started

1. Install [mise](https://mise.en.dev)
2. In the repository root, run:

   ```
   mise trust
   mise install
   ```

## mise

### Settings

Project-level mise settings are configured in `mise.toml` under `[settings]`. Do not modify global config.

To add a setting, run `mise settings add <key> <value>`.

### Adding tools

When adding a tool, use `mise use <tool>` to add it, then run `mise lock` to update `mise.lock`.

### Tasks

Tasks in `mise.toml` should be ordered alphabetically.

## Claude Code

### Settings

When editing Claude Code settings, default to the project-level settings file (`.claude/settings.json`). Only edit user-level settings (`~/.claude/settings.json`) if explicitly asked.

When working in a worktree, edit the project-level settings inside the worktree, not in the main repository.

## Git workflow

- Feature branches: `features/<name>`
- Merge feature branches into main using a merge commit (`git merge --no-ff`), unless otherwise agreed. Use git's default merge commit message.

## Commit size

Each commit should represent one logical change. Do not bundle unrelated changes into a single commit.

## Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

Common types: `feat`, `fix`, `docs`, `refactor`, `chore`, `ci`, `test`, `style`

The description after the colon should be capitalized, unless it begins with a proper noun that has its own casing (e.g. `yt-dlp`, `iPhone`).

### Without scope

```
<type>: <description>
```

### With scope

Scope must be wrapped in parentheses.

```
<type>(<scope>): <description>
```

### Breaking changes

Must be marked with `!` before the colon in the commit title.

```
<type>!: <description>
<type>(<scope>)!: <description>
```

### Examples

```
feat: Add HiBiKi extractor
fix(hibiki): Handle missing episode metadata
feat(hibiki)!: Drop support for legacy stream URLs
```
