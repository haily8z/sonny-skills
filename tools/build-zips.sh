#!/usr/bin/env bash
# Đóng gói mỗi skill thành dist/<skill>.zip (zip chứa đúng 1 thư mục skill ở gốc)
# để upload lên Claude.ai / ChatGPT. Chạy từ gốc repo: bash tools/build-zips.sh
set -euo pipefail
cd "$(dirname "$0")/.."
rm -rf dist && mkdir -p dist
cd skills
for d in */; do
  s="${d%/}"
  zip -qr "../dist/$s.zip" "$s" -x '*.DS_Store' '*__pycache__*'
  echo "dist/$s.zip"
done
