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
skills_destination_root="$repo_root/skills"
agents_destination_root="$repo_root/agents"
dry_run=false

if [[ -n "${CODEX_SKILLS_DIR:-}" ]]; then
  skills_source_root="$CODEX_SKILLS_DIR"
elif [[ -n "${CODEX_HOME:-}" ]]; then
  skills_source_root="$CODEX_HOME/skills"
else
  skills_source_root="${HOME:?HOME is required when CODEX_HOME is unset}/.codex/skills"
fi

if [[ -n "${CODEX_AGENTS_DIR:-}" ]]; then
  agents_source_root="$CODEX_AGENTS_DIR"
elif [[ -n "${CODEX_HOME:-}" ]]; then
  agents_source_root="$CODEX_HOME/agents"
else
  agents_source_root="${HOME:?HOME is required when CODEX_HOME is unset}/.codex/agents"
fi

if [[ -n "${CODEX_HOME:-}" ]]; then
  instructions_source_file="$CODEX_HOME/AGENTS.md"
else
  instructions_source_file="${HOME:?HOME is required when CODEX_HOME is unset}/.codex/AGENTS.md"
fi

usage() {
  printf '%s\n' \
    "Usage: $(basename "$0") [--full] [--dry-run] [--source DIR] [--agents-source DIR] [--instructions-source FILE]" \
    "" \
    "Mirror maintained skills, agent roles, and user instructions into the repository." \
    "Full sync is the default: complete agent files include model and reasoning settings." \
    "" \
    "Options:" \
    "  --full              Explicitly select the default full sync mode." \
    "  --dry-run           Show changes without modifying the repository." \
    "  --source DIR        Override the source skills directory." \
    "  --agents-source DIR Override the source agents directory." \
    "  --instructions-source FILE Override the source user AGENTS.md." \
    "  -h, --help          Show this help message."
}

while (($#)); do
  case "$1" in
    --full)
      ;;
    --dry-run)
      dry_run=true
      ;;
    --source)
      shift
      if (($# == 0)); then
        printf 'error: --source requires a directory\n' >&2
        exit 2
      fi
      skills_source_root="$1"
      ;;
    --agents-source)
      shift
      if (($# == 0)); then
        printf 'error: --agents-source requires a directory\n' >&2
        exit 2
      fi
      agents_source_root="$1"
      ;;
    --instructions-source)
      shift
      if (($# == 0)); then
        printf 'error: --instructions-source requires a file\n' >&2
        exit 2
      fi
      instructions_source_file="$1"
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

[[ -d "$skills_destination_root" ]] || {
  printf 'error: repository skills directory not found: %s\n' "$skills_destination_root" >&2
  exit 1
}

[[ -d "$agents_destination_root" ]] || {
  printf 'error: repository agents directory not found: %s\n' "$agents_destination_root" >&2
  exit 1
}

# Validate every source before changing any destination.
for skill in "${skills[@]}"; do
  [[ -d "$skills_source_root/$skill" ]] || {
    printf 'error: source skill not found: %s\n' "$skills_source_root/$skill" >&2
    exit 1
  }
done

[[ -d "$agents_source_root" ]] || {
  printf 'error: source agents directory not found: %s\n' "$agents_source_root" >&2
  exit 1
}

[[ -f "$instructions_source_file" ]] || {
  printf 'error: user instructions file not found: %s\n' "$instructions_source_file" >&2
  exit 1
}

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
instructions_rsync_args=(-a -i)

if [[ "$dry_run" == true ]]; then
  rsync_args+=(-n)
  instructions_rsync_args+=(-n)
fi

printf 'Sync mode: full (including agent model and reasoning settings)\n'
printf 'Skills source: %s\n' "$skills_source_root"
printf 'Agents source: %s\n' "$agents_source_root"
printf 'User instructions source: %s\n' "$instructions_source_file"
printf 'Repository: %s\n' "$repo_root"

for skill in "${skills[@]}"; do
  printf '\n[%s]\n' "$skill"
  rsync "${rsync_args[@]}" "$skills_source_root/$skill/" "$skills_destination_root/$skill/"
done

printf '\n[agents]\n'
rsync "${rsync_args[@]}" "$agents_source_root/" "$agents_destination_root/"

printf '\n[user-AGENTS.md]\n'
if ! cmp -s "$instructions_source_file" "$repo_root/user-AGENTS.md"; then
  rsync "${instructions_rsync_args[@]}" "$instructions_source_file" "$repo_root/user-AGENTS.md"
fi

if [[ "$dry_run" == true ]]; then
  printf '\nDry run complete.\n'
else
  printf '\nSync complete.\n'
fi
