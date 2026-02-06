#!/bin/bash
# GitHub Pages デプロイ前チェックスクリプト
# 使い方: bash scripts/validate-pages.sh
#
# Cursorから実行: 「bash scripts/validate-pages.sh を実行して」

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

ERRORS=0
WARNINGS=0

error() { echo -e "${RED}[ERROR] $1${NC}"; ERRORS=$((ERRORS + 1)); }
warn()  { echo -e "${YELLOW}[WARN]  $1${NC}"; WARNINGS=$((WARNINGS + 1)); }
ok()    { echo -e "${GREEN}[OK]    $1${NC}"; }

echo "========================================="
echo " GitHub Pages デプロイ前チェック"
echo "========================================="
echo ""

# --- 1. ブランチチェック ---
echo "--- ブランチ確認 ---"
BRANCH=$(git branch --show-current)
if [ "$BRANCH" = "main" ]; then
    ok "mainブランチにいます（デプロイ対象）"
else
    warn "現在 '$BRANCH' ブランチです。GitHub Pagesはmainブランチへのpushでのみデプロイされます"
    echo "    → mainにマージしてからpushしてください"
fi
echo ""

# --- 2. docs/ディレクトリ基本チェック ---
echo "--- docs/ ディレクトリ確認 ---"
if [ -d "docs" ]; then
    ok "docs/ ディレクトリが存在します"
else
    error "docs/ ディレクトリが見つかりません！"
fi

if [ -f "docs/.nojekyll" ]; then
    ok ".nojekyll ファイルが存在します"
else
    error "docs/.nojekyll がありません！Jekyllが有効化され、一部ファイルが無視される可能性があります"
fi

if [ -f "docs/index.html" ]; then
    ok "docs/index.html（トップページ）が存在します"
else
    error "docs/index.html がありません！トップページが404になります"
fi
echo ""

# --- 3. ファイル配置チェック ---
echo "--- ファイル配置チェック ---"

# docs/直下の.htmlファイル（レガシー）を検出
LEGACY_FILES=$(find docs -maxdepth 1 -name "*.html" ! -name "index.html" 2>/dev/null | sort)
if [ -n "$LEGACY_FILES" ]; then
    warn "docs/ 直下にindex.html以外のHTMLファイルがあります（レガシー配置）:"
    echo "$LEGACY_FILES" | while read f; do
        echo "    → $f"
    done
    echo "    ※ 新規作成時は docs/[プロジェクト名]/index.html を使ってください"
else
    ok "docs/ 直下にレガシーHTMLファイルはありません"
fi

# サブディレクトリでindex.html以外をメインファイルにしているケースを検出
NON_INDEX=$(find docs -mindepth 2 -name "*.html" ! -name "index.html" 2>/dev/null | sort)
if [ -n "$NON_INDEX" ]; then
    echo ""
    warn "サブディレクトリにindex.html以外のHTMLがあります:"
    echo "$NON_INDEX" | while read f; do
        DIR=$(dirname "$f")
        if [ ! -f "$DIR/index.html" ]; then
            error "  $f → このディレクトリにindex.htmlがないためフォルダURLでアクセスすると404になります"
        else
            echo "    → $f （index.htmlも存在するので問題なし）"
        fi
    done
fi
echo ""

# --- 4. 拡張子なしファイルチェック ---
echo "--- 拡張子チェック ---"
NO_EXT=$(find docs -maxdepth 2 -type f ! -name ".*" ! -name "*.html" ! -name "*.md" ! -name "*.css" ! -name "*.js" ! -name "*.json" ! -name "*.png" ! -name "*.jpg" ! -name "*.gif" ! -name "*.svg" ! -name "*.ico" ! -name "*.xml" ! -name "*.txt" ! -name "*.pdf" ! -name "CNAME" 2>/dev/null)
if [ -n "$NO_EXT" ]; then
    warn "不明な拡張子のファイルがあります:"
    echo "$NO_EXT" | while read f; do echo "    → $f"; done
else
    ok "不明な拡張子のファイルはありません"
fi
echo ""

# --- 5. index.htmlからのリンク検証 ---
echo "--- トップページのリンク検証 ---"
if [ -f "docs/index.html" ]; then
    # href属性を抽出（外部URLは除外）
    LINKS=$(grep -oP 'href="(?!http|#|mailto)([^"]+)"' docs/index.html | sed 's/href="//;s/"//' | sort -u)
    for link in $LINKS; do
        TARGET="docs/$link"
        # ディレクトリリンク（末尾/）の場合はindex.htmlを確認
        if [[ "$link" == */ ]]; then
            TARGET="docs/${link}index.html"
        fi
        if [ -e "$TARGET" ]; then
            ok "リンク先が存在: $link → $TARGET"
        else
            error "リンク先が見つからない: $link → $TARGET が存在しません！（404になります）"
        fi
    done
else
    error "docs/index.htmlが存在しないため、リンク検証をスキップしました"
fi
echo ""

# --- 6. GitHub Actionsワークフロー確認 ---
echo "--- デプロイ設定確認 ---"
if [ -f ".github/workflows/pages.yml" ]; then
    ok "GitHub Actionsワークフロー (.github/workflows/pages.yml) が存在します"
    if grep -q "path: 'docs'" .github/workflows/pages.yml; then
        ok "デプロイ対象が 'docs' に設定されています"
    else
        error "デプロイ対象が 'docs' 以外になっている可能性があります"
    fi
else
    warn "GitHub Actionsワークフローが見つかりません。リポジトリ設定でPagesのソースを確認してください"
fi
echo ""

# --- 7. コミット状態チェック ---
echo "--- Git状態確認 ---"
DOCS_CHANGES=$(git status --porcelain docs/ 2>/dev/null)
if [ -n "$DOCS_CHANGES" ]; then
    warn "docs/ に未コミットの変更があります:"
    echo "$DOCS_CHANGES" | while read f; do echo "    → $f"; done
    echo "    ※ コミット＆プッシュしないとデプロイに反映されません"
else
    ok "docs/ に未コミットの変更はありません"
fi
echo ""

# --- 結果サマリー ---
echo "========================================="
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN} 全チェック合格！デプロイの準備ができています${NC}"
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW} 警告 ${WARNINGS}件（デプロイは可能ですが確認推奨）${NC}"
else
    echo -e "${RED} エラー ${ERRORS}件 / 警告 ${WARNINGS}件${NC}"
    echo -e "${RED} デプロイ前にエラーを修正してください${NC}"
fi
echo "========================================="

exit $ERRORS
