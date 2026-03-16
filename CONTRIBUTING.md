# Contributing to AI News Digest

Thanks for your interest in contributing! This project automates daily AI news digests via Claude Code.

## Getting Started

1. Fork and clone the repo
2. Copy `.env.example` → `.env` and fill in credentials
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install system dependencies (see README for details)

## Development

- Python scripts live in `scripts/yt/`
- Slash commands live in `.claude/commands/`
- State files in `.state/` are gitignored — never commit them
- Test your changes locally before opening a PR:
  ```bash
  pre-commit run --all-files
  ```

## Adding a New Digest Type

1. Create a slash command in `.claude/commands/ai-news-digest-<type>.md`
2. Add helper scripts under `scripts/<type>/`
3. Add a state file entry in `.state/last-digest-<type>.json`
4. Update `CLAUDE.md` with the new digest's structure and usage
5. Update `README.md` with setup and usage instructions

## Pull Requests

- Keep PRs focused — one feature or fix per PR
- Follow existing code style and patterns
- Update documentation if your change affects usage
- Ensure `pre-commit run --all-files` passes before submitting
