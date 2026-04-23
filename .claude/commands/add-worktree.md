Fetch origin, then create a new branch `features/$ARGUMENTS[0]` from whichever is ahead between `origin/main` and local `main`, and a worktree at `.claude/worktrees/$ARGUMENTS[0]`.

Steps:
1. Validate that `$ARGUMENTS[0]` matches `^[a-z0-9-]+$`. If it doesn't, stop and report an error — do not proceed.
2. `git fetch origin`
3. Compare `origin/main` and `main` to determine which is ahead using `git rev-list --count main..origin/main` and `git rev-list --count origin/main..main`. Use whichever ref has more commits ahead of the other. If equal, use `origin/main`.
4. `git worktree add .claude/worktrees/$ARGUMENTS[0] -b features/$ARGUMENTS[0] <chosen-ref>`
5. Switch to the new worktree at `.claude/worktrees/$ARGUMENTS[0]` and work from there going forward.
