# AI News Digest

Automated daily AI news digest powered by Claude Code's `/loop` feature. Gathers international AI news across 6 categories, summarizes them bilingually (English titles + Traditional Chinese summaries), and posts a formatted digest to Slack.

## Setup

1. Copy `.env.example` to `.env` and fill in your Slack credentials:
   ```bash
   cp .env.example .env
   ```

2. Required environment variables:
   - `SLACK_BOT_TOKEN` — Slack Bot Token (`xoxb-...`) with `chat:write` scope
   - `SLACK_CHANNEL_ID` — Channel ID for `#update-vibe`
   - `SLACK_WEBHOOK_URL` — (Optional) Webhook fallback

3. Invite your Slack bot to `#update-vibe`:
   ```
   /invite @YourBotName
   ```

## Usage

Run once manually:
```
/ai-news-digest
```

Run on a recurring 24-hour schedule:
```
/loop 24h /ai-news-digest
```

## How It Works

1. **WebSearch** — 12 searches across 6 AI news categories
2. **WebFetch** — Fetches top 2-3 articles per category for details
3. **Dedup** — Checks `.state/last-digest.json` to skip previously posted articles
4. **Format** — Builds Slack mrkdwn with English titles + Traditional Chinese summaries
5. **Post** — Sends to Slack via Bot Token (webhook fallback)
6. **Save State** — Writes posted URLs for next run's deduplication

## News Categories

| Emoji | Category |
|-------|----------|
| 🧠 | LLM / Foundation Models |
| 📦 | AI Products & Applications |
| ⚖️ | AI Policy & Regulation |
| 🔬 | AI Research Papers |
| 💼 | Industry & Business |
| 🔓 | Open Source AI |

## Limitations

- `/loop` has a max duration of ~3 days — restart periodically
- WebSearch availability may vary by region
- Slack `chat.postMessage` has ~4000 char limit per message — digest auto-splits if needed
