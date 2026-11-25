#!/usr/bin/env bash
# Wait until GitHub Pages has finished publishing the current head of
# gh-pages. Every workflow that pushes to gh-pages runs this right before its
# push.
#
# Why: each push to gh-pages starts GitHub's "pages build and deployment"
# run. A push that arrives while that run is still busy makes GitHub cancel
# it, and the cancelled run is reported as a failed deployment (also on the
# repository's front page), although the next run publishes everything a
# minute later. Merging a PR pushes twice in a row (preview removal and the
# "dev" docs), so this used to happen on every merge.
#
# If another push slips in between this check and the caller's push, the
# caller's push is rejected because gh-pages moved; the callers then redo
# their change on top of the new gh-pages and wait here again.
#
# Usage: bash .github/scripts/wait-for-pages.sh
# Env:   GH_TOKEN with `actions: read`, GITHUB_REPOSITORY (set by Actions),
#        PAGES_BRANCH (default gh-pages),
#        PAGES_WAIT_TIMEOUT: give up waiting after this many seconds
#          (default 900),
#        PAGES_RUN_APPEAR_TIMEOUT: continue if no Pages run shows up for the
#          current head within this many seconds (default 120),
#        PAGES_POLL_INTERVAL: seconds between checks (default 10).
# Always exits 0: waiting is a courtesy, never a reason to fail a deploy.
set -uo pipefail

branch="${PAGES_BRANCH:-gh-pages}"
timeout="${PAGES_WAIT_TIMEOUT:-900}"
appear_timeout="${PAGES_RUN_APPEAR_TIMEOUT:-120}"
interval="${PAGES_POLL_INTERVAL:-10}"
start=$SECONDS
unseen_head=""
unseen_since=0
failures=0

while :; do
  # (On HTTP errors `gh api` prints the error body to stdout, so check both
  # its exit status and the value.)
  if ! head="$(gh api "repos/$GITHUB_REPOSITORY/branches/$branch" \
      --jq .commit.sha 2>/dev/null)" \
    || ! [[ "$head" =~ ^[0-9a-f]{40}$ ]]; then
    echo "Could not read $branch; not waiting for GitHub Pages."
    exit 0
  fi

  # GitHub's Pages runs have the event "dynamic" and the pushed commit as
  # their head.
  if state="$(gh api \
    "repos/$GITHUB_REPOSITORY/actions/runs?head_sha=$head&event=dynamic&per_page=1" \
    --jq '.workflow_runs[0].status // "not started"' 2>/dev/null)"; then
    failures=0
  else
    failures=$((failures + 1))
    if [ "$failures" -ge 3 ]; then
      echo "Could not look up GitHub Pages runs; not waiting any longer."
      exit 0
    fi
    state="unknown"
  fi

  if [ "$state" = "completed" ]; then
    echo "GitHub Pages has finished publishing $branch ${head:0:7}."
    exit 0
  fi

  if [ "$state" = "not started" ]; then
    # The Pages run of a push shows up a few seconds after it. If none
    # appears at all, there is nothing to wait for.
    if [ "$head" != "$unseen_head" ]; then
      unseen_head="$head"
      unseen_since=$SECONDS
    elif [ $((SECONDS - unseen_since)) -ge "$appear_timeout" ]; then
      echo "No GitHub Pages run appeared for $branch ${head:0:7};" \
        "continuing."
      exit 0
    fi
  fi

  waited=$((SECONDS - start))
  if [ "$waited" -ge "$timeout" ]; then
    echo "GitHub Pages is still busy with $branch ${head:0:7} ($state)" \
      "after ${waited}s; continuing anyway."
    exit 0
  fi
  echo "GitHub Pages is busy with $branch ${head:0:7} ($state);" \
    "checking again in ${interval}s."
  sleep "$interval"
done
