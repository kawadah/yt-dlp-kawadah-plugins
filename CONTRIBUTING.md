# CONTRIBUTING.md

## Git workflow

- Feature branches: `features/<name>`

## Commit messages

Each commit should represent one logical change. Do not bundle unrelated changes into a single commit.

Follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

Common types: `feat`, `fix`, `docs`, `refactor`, `chore`, `ci`, `test`

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
<type>[(<scope>)]!: <description>
```

### Examples

```
feat: add HiBiKi extractor
fix(hibiki): handle missing episode metadata
feat(hibiki)!: drop support for legacy stream URLs
```
