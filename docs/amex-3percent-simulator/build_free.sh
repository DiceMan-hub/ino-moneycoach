#!/bin/bash
# simulator_pro.html → index.html (無料版) を生成
#
# ルール:
#   PRO-START 〜 PRO-END       → 削除（PRO専用機能）
#   FREE-ONLY-START / END      → マーカー行だけ削除（中身は残す）
#   /* <!-- PRO-START --> */ 等 → CSS内のPROブロックも削除
#   title / OGP               → 無料版用に置換
#
# 使い方: bash build_free.sh

SRC="simulator_pro.html"
DST="index.html"
DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$DIR"

if [ ! -f "$SRC" ]; then
  echo "Error: $SRC not found"
  exit 1
fi

# 1. PRO-START〜PRO-END を削除（HTML/CSS/JSすべて対応）
# 2. FREE-ONLY-START / FREE-ONLY-END のマーカー行だけ削除
# 3. title / OGP を無料版用に置換
sed \
  -e '/PRO-START/,/PRO-END/d' \
  -e '/FREE-ONLY-START/d' \
  -e '/FREE-ONLY-END/d' \
  -e 's|<title>.*</title>|<title>アメックス 3%還元シミュレーター｜年間ポイント・マイルを自動計算</title>|' \
  -e 's|content="アメックスの3%還元対象店.*シミュレーション。"|content="アメックス6カードの3%還元ポイントを自動計算。ANA・提携航空・Marriott・Hiltonのマイル交換先比較も。"|' \
  -e 's|content="アメックス 3%還元シミュレーター PRO｜300+店舗検索"|content="アメックス 3%還元シミュレーター｜ポイント自動計算"|' \
  -e 's|content="Amazon Pay対応300+店舗を検索。.*シミュレーション。"|content="アメックス6カードの3%還元ポイントを自動計算。マイル交換先比較・実質還元率をリアルタイムでシミュレーション。"|' \
  "$SRC" > "$DST"

echo "Generated: $DST"
echo "  Source:  $SRC ($(wc -l < "$SRC" | tr -d ' ') lines)"
echo "  Output:  $DST ($(wc -l < "$DST" | tr -d ' ') lines)"
