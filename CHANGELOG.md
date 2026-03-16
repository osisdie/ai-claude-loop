# Changelog

All notable changes to this project will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/).

## [0.4.0] - 2026-03-16

### Added
- MIT LICENSE
- `requirements.txt` for Python dependencies
- `CONTRIBUTING.md` with development and PR guidelines
- README: shields.io badges (license, Python, CI, last commit)
- README: demo screenshot section
- README: system dependencies table and `pip install` step

## [0.3.0] - 2026-03-16

### Added
- Video links in combined digest markdown and PDF output

### Changed
- Publisher and published date shown in YT digest output

## [0.2.0] - 2026-03-13

### Added
- CI and lint configuration (pre-commit, ruff, shellcheck)
- Per-step state tracking for YT digest (resume on partial failure)
- Video date metadata in YT digest output

## [0.1.0] - 2026-03-11

### Added
- `/ai-news-digest-yt` command — YouTube digest pipeline
- Transcript extraction (subtitles → Whisper fallback)
- HTML + PDF generation via headless Chrome
- Backblaze B2 upload with presigned URLs
- Thumbnail support in digest output

## [0.0.1] - 2026-03-08

### Added
- `/ai-news-digest-news` command — web news digest
- Bilingual summaries (English + Traditional Chinese)
- Slack posting via Bot Token with webhook fallback
- 6 AI news categories
- News freshness filtering and deduplication
