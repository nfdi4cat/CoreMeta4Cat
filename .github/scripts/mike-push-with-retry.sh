#!/usr/bin/env bash
# Run a mike command that commits to the local gh-pages branch (WITHOUT
# --push), then push gh-pages once GitHub Pages is idle, and start over if the
# push is rejected because gh-pages moved meanwhile.
#
# Why: other workflows push to gh-pages too. Merging a PR with a documentation
# preview starts this deploy and the preview removal in
# deploy_docs_preview.yaml at the same moment. And a push that arrives while
# GitHub Pages is still publishing an earlier one makes GitHub cancel that
# run, which is reported as a failed deployment (see wait-for-pages.sh). So
# this script, not mike, does the push, right after waiting for Pages.
#
# mike never fetches. It commits on top of the local gh-pages branch, compares
# that only with origin/gh-pages as last fetched, and refuses to run when the
# two have diverged. So before every attempt, refresh origin/gh-pages and
# reset the local branch to it (a rejected attempt leaves its commit there).
#
# Usage: bash .github/scripts/mike-push-with-retry.sh <command> [args...]
#        e.g. ... uv run mike deploy --update-aliases 1.2.0 latest
# Env:   MIKE_PUSH_ATTEMPTS (default 3), MIKE_REMOTE (default origin),
#        MIKE_BRANCH (default gh-pages), plus what wait-for-pages.sh needs
#        (GH_TOKEN with `actions: read`).
set -uo pipefail

attempts="${MIKE_PUSH_ATTEMPTS:-3}"
remote="${MIKE_REMOTE:-origin}"
branch="${MIKE_BRANCH:-gh-pages}"
here="$(cd "$(dirname "$0")" && pwd)"

for arg in "$@"; do
  if [ "$arg" = "--push" ]; then
    echo "::error::Pass the mike command without --push; this script" \
      "pushes once GitHub Pages is idle."
    exit 2
  fi
done

for attempt in $(seq 1 "$attempts"); do
  if git ls-remote --exit-code --heads "$remote" "$branch" > /dev/null; then
    git fetch --quiet "$remote" \
      "+refs/heads/$branch:refs/remotes/$remote/$branch" || exit 1
    git branch --force --no-track "$branch" "$remote/$branch" || exit 1
  fi

  # Builds the docs and commits them to the local gh-pages branch.
  "$@" || exit $?

  PAGES_BRANCH="$branch" bash "$here/wait-for-pages.sh"
  if git push --quiet "$remote" "refs/heads/$branch:refs/heads/$branch"; then
    exit 0
  fi
  if [ "$attempt" -lt "$attempts" ]; then
    echo "$branch moved while deploying (attempt $attempt of $attempts);" \
      "redoing the deploy on top of the new $branch."
  fi
done

echo "::error::Could not push to $branch after $attempts attempts; it kept" \
  "changing during the deploy."
exit 1
