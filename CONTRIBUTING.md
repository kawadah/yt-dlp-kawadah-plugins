# CONTRIBUTING.md

## Git workflow

- Feature branches: `features/<name>`

## Commit messages

Each commit should represent one logical change. Do not bundle unrelated changes into a single commit.

Follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

```
<type>[optional scope]: <description>
```

Common types: `feat`, `fix`, `docs`, `refactor`, `chore`, `ci`, `test`

Breaking changes: append `!` before the colon (e.g. `feat!: ...`) or add a `BREAKING CHANGE:` footer.
