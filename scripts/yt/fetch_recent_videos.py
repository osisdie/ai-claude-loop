#!/usr/bin/env python3
"""
Fetch recent videos from a YouTube channel, filtered to last 24h.

Usage:
  python scripts/yt/fetch_recent_videos.py [--channel URL] [--hours 24] [--state PATH]

Outputs JSON array to stdout:
  [{"id": "abc123", "title": "Video Title", "upload_date": "20260311"}, ...]
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

DEFAULT_CHANNEL = "https://www.youtube.com/@AIDailyBrief"


def fetch_channel_videos(channel_url: str, max_items: int = 10) -> list[dict]:
    """Fetch recent videos with full metadata (non-flat to get upload_date).

    Uses --playlist-items to limit scope since non-flat mode is slower.
    """
    cmd = [
        "yt-dlp",
        "--playlist-items", f"1:{max_items}",
        "--print", "%(id)s\t%(title)s\t%(upload_date)s",
        "--skip-download",
        f"{channel_url}/videos",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if result.returncode != 0:
        print(f"yt-dlp failed: {result.stderr[:500]}", file=sys.stderr)
        sys.exit(1)

    videos = []
    for line in result.stdout.strip().splitlines():
        parts = line.split("\t", 2)
        if len(parts) >= 2:
            vid = {
                "id": parts[0],
                "title": parts[1],
                "upload_date": parts[2] if len(parts) == 3 else "NA",
            }
            videos.append(vid)
    return videos


def filter_recent(videos: list[dict], hours: int) -> list[dict]:
    """Keep only videos uploaded within the last N hours."""
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    cutoff_str = cutoff.strftime("%Y%m%d")

    recent = []
    for v in videos:
        date_str = v.get("upload_date", "NA")
        if date_str == "NA":
            continue
        # yt-dlp dates are YYYYMMDD; include if >= cutoff date
        if date_str >= cutoff_str:
            recent.append(v)
    return recent


def dedup(videos: list[dict], state_path: Path) -> list[dict]:
    """Remove videos already posted (by video ID)."""
    if not state_path.exists():
        return videos

    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return videos

    posted_ids = set(state.get("posted_video_ids", []))
    return [v for v in videos if v["id"] not in posted_ids]


def main():
    parser = argparse.ArgumentParser(description="Fetch recent YouTube videos")
    parser.add_argument("--channel", default=DEFAULT_CHANNEL, help="Channel URL")
    parser.add_argument("--hours", type=int, default=24, help="Lookback window")
    parser.add_argument(
        "--state",
        default=".state/last-digest-yt.json",
        help="State file for dedup",
    )
    args = parser.parse_args()

    print(f"Fetching videos from {args.channel}...", file=sys.stderr)
    all_videos = fetch_channel_videos(args.channel)
    print(f"Found {len(all_videos)} total videos", file=sys.stderr)

    recent = filter_recent(all_videos, args.hours)
    print(f"After {args.hours}h filter: {len(recent)} videos", file=sys.stderr)

    new_videos = dedup(recent, Path(args.state))
    print(f"After dedup: {len(new_videos)} new videos", file=sys.stderr)

    json.dump(new_videos, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
