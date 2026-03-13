# AI News Digest

Automated daily AI news digest that posts to Slack `#update-vibe`.

## Project Structure

```
.claude/commands/ai-news-digest-news.md  — Slash command for news gathering + posting
scripts/slack_notify.sh             — Slack posting utility (Bot Token + webhook fallback)
digest-news/YYYY-MM-DD/             — Local backup (gitignored)
.state/last-digest-news.json             — Dedup state (not committed)
```

## Usage

```
/ai-news-digest-news          # Run once manually
/loop 24h /ai-news-digest-news  # Run every 24 hours
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

## YouTube Digest (`/ai-news-digest-yt`)

Fetches recent videos from [@AIDailyBrief](https://www.youtube.com/@AIDailyBrief), extracts transcripts, generates bilingual summaries (EN + zh-TW), builds HTML/PDF, uploads PDFs to Backblaze B2, and posts to Slack.

```
.claude/commands/ai-news-digest-yt.md  — Slash command for YT digest
scripts/yt/fetch_recent_videos.py      — List recent videos (yt-dlp + 24h filter + dedup)
scripts/yt/get_transcript.py           — Extract transcript (subs → Whisper fallback)
scripts/yt/build_html.py               — Markdown → styled HTML
scripts/yt/build_pdf.py                — HTML → PDF (headless Chrome)
scripts/yt/upload_b2.py                — Upload to Backblaze B2, returns download URL
digest-yt/YYYY-MM-DD/                  — Local output (gitignored)
.state/last-digest-yt.json             — Dedup state (not committed)
```

### B2 Storage

- Bucket: `claw-dir`
- Path: `ai-digest-yt/YYYY-MM-DD/summary_en_YYYYMMDD.pdf`
- URL: `https://f005.backblazeb2.com/file/claw-dir/ai-digest-yt/...`

## State Tracking

- `.state/last-digest-news.json` tracks posted URLs for deduplication (news digest)
- `.state/last-digest-yt.json` tracks posted video IDs + per-video step completion for deduplication and resume (YT digest)
  - `posted_video_ids`: videos fully completed (all steps including slack_post)
  - `video_status`: per-video step booleans (transcript, thumbnail, summary, html, pdf, b2_upload, slack_post) — enables resume on partial failure
  - Incomplete videos stay in `video_status` but NOT in `posted_video_ids` → re-fetched on retry
- Keep max 30 entries (current + previous digest)
- State directory is gitignored
