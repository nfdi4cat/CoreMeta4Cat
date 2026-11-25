#!/usr/bin/env bash
# Add, update or remove the documentation preview of a PR on gh-pages
# (pr-preview/pr-<number>/). Used by deploy_docs_preview.yaml.
#
# Run it inside a checkout of gh-pages; the workflow checks out only the
# preview's folder. The push waits until GitHub Pages is idle
# (wait-for-pages.sh). If it is rejected because gh-pages moved meanwhile,
# the change is redone on top of the new gh-pages.
#
# Removing deletes the whole folder. (pr-preview-action, used before, kept
# each preview's .nojekyll, so every removed preview left an empty folder.)
#
# Usage: bash publish-preview.sh deploy <pr-number> <site-dir>
#        bash publish-preview.sh remove <pr-number>
# Env:   PAGES_BRANCH (default gh-pages), plus what wait-for-pages.sh needs.
# Writes changed=true|false to $GITHUB_OUTPUT.
set -euo pipefail

action="${1:-}"
pr="${2:-}"
site="${3:-}"
branch="${PAGES_BRANCH:-gh-pages}"
dir="pr-preview/pr-$pr"
here="$(cd "$(dirname "$0")" && pwd)"
attempts=3

if ! [[ "$pr" =~ ^[0-9]+$ ]]; then
  echo "::error::Invalid PR number '$pr'."
  exit 2
fi
case "$action" in
  deploy)
    if [ ! -d "$site" ]; then
      echo "::error::Site directory '$site' not found."
      exit 2
    fi
    site="$(cd "$site" && pwd)"
    message="Deploy preview for PR $pr"
    ;;
  remove)
    message="Remove preview for PR $pr"
    ;;
  *)
    echo "Usage: $0 deploy <pr-number> <site-dir> | remove <pr-number>" >&2
    exit 2
    ;;
esac

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

output() { echo "$1" >> "${GITHUB_OUTPUT:-/dev/null}"; }

for attempt in $(seq 1 "$attempts"); do
  if [ "$attempt" -gt 1 ]; then
    git fetch --quiet --depth=1 origin "$branch"
    git reset --quiet --hard FETCH_HEAD
  fi

  if [ "$action" = "deploy" ]; then
    rm -rf "$dir"
    mkdir -p "$dir"
    cp -R "$site/." "$dir/"
    # GitHub Pages only reads these at the root of gh-pages.
    rm -f "$dir/.nojekyll" "$dir/CNAME"
    git add --all -- "$dir"
  else
    git rm -r --quiet --ignore-unmatch -- "$dir"
  fi

  if git diff --cached --quiet; then
    echo "Nothing to change in $dir on $branch."
    output "changed=false"
    exit 0
  fi
  git commit --quiet -m "$message"

  bash "$here/wait-for-pages.sh"
  if git push --quiet origin "HEAD:refs/heads/$branch"; then
    echo "$message: pushed to $branch."
    output "changed=true"
    exit 0
  fi
  echo "$branch moved meanwhile (attempt $attempt of $attempts);" \
    "redoing the change on top of it."
done

echo "::error::Could not push to $branch after $attempts attempts."
exit 1
