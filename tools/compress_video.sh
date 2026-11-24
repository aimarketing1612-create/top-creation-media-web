#!/usr/bin/env bash
# Shrinks a big video into a website-ready MP4 (1080p, H.264, about 6-15 MB for 30-40 s).
# Needs ffmpeg:  Mac: brew install ffmpeg   Windows: winget install ffmpeg
#
#   bash tools/compress_video.sh ~/Desktop/home-video.mp4 home
#
# Writes deploy/assets/video/<name>.mp4 and a cover image deploy/assets/video/<name>-cover.jpg.
# Then set  mp4: '/assets/video/<name>.mp4'  and  poster: '/assets/video/<name>-cover.jpg'
# for that video in deploy/site-media.js (or send me the files / YouTube link).
set -euo pipefail
in="${1:?usage: compress_video.sh <input video> <name, e.g. home>}"
name="${2:?usage: compress_video.sh <input video> <name, e.g. home>}"
out="$(cd "$(dirname "$0")/.." && pwd)/deploy/assets/video"
mkdir -p "$out"
ffmpeg -y -i "$in" -vf "scale='min(1920,iw)':-2,fps=30" \
  -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -profile:v high \
  -c:a aac -b:a 96k -ac 2 -movflags +faststart "$out/$name.mp4"
ffmpeg -y -ss 1 -i "$out/$name.mp4" -frames:v 1 -q:v 3 "$out/$name-cover.jpg"
ls -lh "$out/$name.mp4" "$out/$name-cover.jpg"
