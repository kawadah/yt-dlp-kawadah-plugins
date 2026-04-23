# CLAUDE.md

Read @README.md and @CONTRIBUTING.md first. CLAUDE.md defines instructions specifically to Claude Code.

## Project structure

```
yt_dlp_plugins/
  extractor/   # InfoExtractor subclasses (class names must end in IE)
  postprocessor/  # PostProcessor subclasses (class names must end in PP)
```

Follows the [yt-dlp-sample-plugins](https://github.com/yt-dlp/yt-dlp-sample-plugins) layout. Uses `find_namespace:` so **no `__init__.py`** in any `yt_dlp_plugins` directory.

## Worktrees

Use `claude -w <name>` to create a worktree. Claude Code's default worktree directory is `.claude/worktrees/` (ignored by `.gitignore`).

## Commits

When 2 or more files with unrelated changes are pending, suggest making separate commits.

## File system rules

- **NEVER write outside the project directory** — no `/tmp`, `~`, or any external path
- Temporary files go in `.tmp/` inside the repo (ignored by `.gitignore`); clean up after use
