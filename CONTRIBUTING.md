# CONTRIBUTING.md

## Git workflow

- Feature branches: `features/<name>`
- Worktrees live inside the repo at `.claude/worktrees/<name>` — use `claude -w <name>` to create them (ignored by `.gitignore`)

## Commit messages

Follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

```
<type>[optional scope]: <description>
```

Common types: `feat`, `fix`, `docs`, `refactor`, `chore`, `ci`, `test`

Breaking changes: append `!` before the colon (e.g. `feat!: ...`) or add a `BREAKING CHANGE:` footer.
