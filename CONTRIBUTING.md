# CONTRIBUTING

See [yt-dlp's wiki on plugin development](https://github.com/yt-dlp/yt-dlp/wiki/Plugin-Development).

## Getting started

1. Install [mise](https://mise.jdx.dev)
2. In the repository root, run:

   ```
   mise trust
   mise install
   ```

## mise tasks

Tasks in `mise.toml` are ordered alphabetically.

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
<type>[(<scope>)]!: <description>
```

### Examples

```
feat: Add HiBiKi extractor
fix(hibiki): Handle missing episode metadata
feat(hibiki)!: Drop support for legacy stream URLs
```
