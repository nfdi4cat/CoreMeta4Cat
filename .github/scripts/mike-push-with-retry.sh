#!/usr/bin/env bash
# Run a mike command that pushes to gh-pages (e.g. `uv run mike deploy --push ...`)
# and retry it when the push is rejected because gh-pages moved meanwhile.
#
# Why: other workflows push to gh-pages too. Merging a PR with a documentation
# preview starts this deploy and the preview removal in
# deploy_docs_preview.yaml at the same moment, and the removal usually pushes
# while the docs are still being built.
#
# mike never fetches. It commits on top of the local gh-pages branch, compares
# that only with origin/gh-pages as last fetched, and refuses to run when the
# two have diverged. So before every attempt, refresh origin/gh-pages and
# reset the local branch to it (a rejected attempt leaves its commit there).
#
# Usage: bash .github/scripts/mike-push-with-retry.sh <command> [args...]
# Env:   MIKE_PUSH_ATTEMPTS (default 3), MIKE_REMOTE (default origin),
#        MIKE_BRANCH (default gh-pages)
set -uo pipefail

attempts="${MIKE_PUSH_ATTEMPTS:-3}"
remote="${MIKE_REMOTE:-origin}"
branch="${MIKE_BRANCH:-gh-pages}"
log="$(mktemp)"
trap 'rm -f "$log"' EXIT

for attempt in $(seq 1 "$attempts"); do
  if git ls-remote --exit-code --heads "$remote" "$branch" > /dev/null; then
    git fetch --quiet "$remote" "+refs/heads/$branch:refs/remotes/$remote/$branch" || exit 1
    git branch --force --no-track "$branch" "$remote/$branch" || exit 1
  fi

  "$@" 2>&1 | tee "$log"
  status=${PIPESTATUS[0]}
  if [ "$status" -eq 0 ]; then
    exit 0
  fi

  # Only a rejected push is worth repeating; a broken build fails right away.
  if ! grep -q "failed to push branch" "$log"; then
    exit "$status"
  fi
  if [ "$attempt" -lt "$attempts" ]; then
    echo "::warning::$branch changed while deploying (attempt $attempt of $attempts); retrying on top of the new $branch."
    sleep $((attempt * 10))
  fi
done

echo "::error::Could not push to $branch after $attempts attempts; it kept changing during the deploy."
exit 1
