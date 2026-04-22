# CLAUDE.md

## Project structure

```
yt_dlp_plugins/
  extractor/   # InfoExtractor subclasses (class names must end in IE)
  postprocessor/  # PostProcessor subclasses (class names must end in PP)
```

Follows the [yt-dlp-sample-plugins](https://github.com/yt-dlp/yt-dlp-sample-plugins) layout. Uses `find_namespace:` so **no `__init__.py`** in any `yt_dlp_plugins` directory.

## File system rules

- **NEVER write outside the project directory** — no `/tmp`, `~`, or any external path
- Temporary files go in `.tmp/` inside the repo (ignored by `.gitignore`); clean up after use

## Git workflow

- Feature branches: `features/<name>`
- Worktrees live inside the repo at `.claude/worktrees/<name>` — use `claude -w <name>` to create them (ignored by `.gitignore`)
