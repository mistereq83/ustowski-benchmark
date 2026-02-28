#!/bin/bash
# Build and deploy
cd "$(dirname "$0")"
python3 build.py
git add -A
git commit -m "Build: $(date '+%Y-%m-%d %H:%M')" 2>/dev/null
git push origin main
echo "✅ Built and pushed!"
