Remove the worktree `.claude/worktrees/$ARGUMENTS[0]` and delete the branch `features/$ARGUMENTS[0]`.

Steps:
1. Validate that `$ARGUMENTS[0]` matches `^[a-z0-9-]+$`. If it doesn't, stop and report an error — do not proceed.
2. Check if `features/$ARGUMENTS[0]` has any commits not present in `main` or `origin/main` using `git log main..features/$ARGUMENTS[0]` and `git log origin/main..features/$ARGUMENTS[0]`.
3. If there are unmerged commits, warn the user and ask for confirmation before proceeding. Stop if they decline.
4. `git worktree remove .claude/worktrees/$ARGUMENTS[0]`
5. `git branch -d features/$ARGUMENTS[0]`
