#!/usr/bin/env bash

set -euo pipefail

skills=(
  commit
  deliver-with-evidence
  design-delivery-plan
  markitdown
)

script_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
repo_root="$(CDPATH= cd -- "$script_dir/.." && pwd)"
destination_root="$repo_root/skills"
dry_run=false

if [[ -n "${CODEX_SKILLS_DIR:-}" ]]; then
  source_root="$CODEX_SKILLS_DIR"
elif [[ -n "${CODEX_HOME:-}" ]]; then
  source_root="$CODEX_HOME/skills"
else
  source_root="${HOME:?HOME is required when CODEX_HOME is unset}/.codex/skills"
fi

usage() {
  printf '%s\n' \
    "Usage: $(basename "$0") [--dry-run] [--source DIR]" \
    "" \
    "Mirror the repository's four maintained skills from a Codex skills directory." \
    "" \
    "Options:" \
    "  --dry-run     Show changes without modifying the repository." \
    "  --source DIR  Override the source skills directory." \
    "  -h, --help    Show this help message."
}

while (($#)); do
  case "$1" in
    --dry-run)
      dry_run=true
      ;;
    --source)
      shift
      if (($# == 0)); then
        printf 'error: --source requires a directory\n' >&2
        exit 2
      fi
      source_root="$1"
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'error: unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
  shift
done

command -v rsync >/dev/null 2>&1 || {
  printf 'error: rsync is required\n' >&2
  exit 1
}

[[ -d "$destination_root" ]] || {
  printf 'error: repository skills directory not found: %s\n' "$destination_root" >&2
  exit 1
}

# Validate every source before changing any destination.
for skill in "${skills[@]}"; do
  [[ -d "$source_root/$skill" ]] || {
    printf 'error: source skill not found: %s\n' "$source_root/$skill" >&2
    exit 1
  }
done

rsync_args=(
  -a
  -i
  --delete
  --delete-excluded
  --exclude
  '__pycache__/'
  --exclude
  '*.pyc'
)

if [[ "$dry_run" == true ]]; then
  rsync_args+=(-n)
fi

printf 'Source: %s\n' "$source_root"
printf 'Destination: %s\n' "$destination_root"

for skill in "${skills[@]}"; do
  printf '\n[%s]\n' "$skill"
  rsync "${rsync_args[@]}" "$source_root/$skill/" "$destination_root/$skill/"
done

if [[ "$dry_run" == true ]]; then
  printf '\nDry run complete.\n'
else
  printf '\nSync complete.\n'
fi
