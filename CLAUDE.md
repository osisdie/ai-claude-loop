# AI News Digest

Automated daily AI news digest that posts to Slack `#update-vibe`.

## Project Structure

```
.claude/commands/ai-news-digest.md  — Slash command for news gathering + posting
scripts/slack_notify.sh             — Slack posting utility (Bot Token + webhook fallback)
.state/last-digest.json             — Dedup state (not committed)
```

## Usage

```
/ai-news-digest          # Run once manually
/loop 24h /ai-news-digest  # Run every 24 hours
```

## Slack Formatting

- Use Slack mrkdwn syntax (not markdown): `*bold*`, `_italic_`, `>` for quotes
- Links: `<https://url|Display Text>`
- Emojis: `:emoji_name:` syntax
- Keep messages under 3800 chars; split if needed

## News Categories

1. :brain: LLM / Foundation Models
2. :package: AI Products & Applications
3. :scales: AI Policy & Regulation
4. :microscope: AI Research Papers
5. :briefcase: Industry & Business
6. :unlock: Open Source AI

## Bilingual Format

- Article titles: English (original)
- Summaries: Traditional Chinese (繁體中文), 1-2 sentences

## State Tracking

- `.state/last-digest.json` tracks posted URLs for deduplication
- Keep max 30 URLs (current + previous digest)
- State directory is gitignored
