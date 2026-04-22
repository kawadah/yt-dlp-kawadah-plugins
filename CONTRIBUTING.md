# CONTRIBUTING

See [yt-dlp's wiki on plugin development](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development).

## Getting started

1. Install [mise](https://mise.jdx.dev)
2. In the repository root, run:

   ```
   mise trust
   mise install
   ```

## Git workflow

- Feature branches: `features/<name>`
- Merge feature branches into main using a merge commit (`git merge --no-ff`), unless otherwise agreed. Use git's default merge commit message.

## Commit size

Each commit should represent one logical change. Do not bundle unrelated changes into a single commit.

## Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

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
