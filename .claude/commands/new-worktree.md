Fetch origin, then create a new branch `features/$ARGUMENTS[0]` from `origin/main`, and a worktree at `.claude/worktrees/$ARGUMENTS[0]`.

Steps:
1. Validate that `$ARGUMENTS[0]` matches `^[a-z0-9-]+$`. If it doesn't, stop and report an error — do not proceed.
2. `git fetch origin`
2. `git worktree add .claude/worktrees/$ARGUMENTS[0] -b features/$ARGUMENTS[0] origin/main`
3. Switch to the new worktree at `.claude/worktrees/$ARGUMENTS[0]` and work from there going forward.
