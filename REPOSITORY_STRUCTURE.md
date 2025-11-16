# リポジトリ構造の整理方針

## 現在の問題点

1. **ルートディレクトリにHTMLファイルが散在**
   - `amex-benefits-2025.html`
   - `ana-upgrade-analysis.html`
   - `hilton-honors-japan-guide.html`
   - など多数

2. **テストファイルが残っている**
   - `TEST.html`, `TEST2.html`, `TEST_new.html`

3. **重複ファイルの可能性**
   - 同じコンテンツが複数の場所にある可能性

## 推奨される整理方針

### ディレクトリ構造

```
/
├── .github/              # GitHub Actions設定
│   └── workflows/
│       └── pages.yml
│
├── content/              # VectorDB用のMarkdownコンテンツ（唯一の元データ）
│   ├── guides/           # ガイド系コンテンツ
│   │   └── jre-point-strategy.md
│   ├── blog/             # ブログ記事（将来）
│   ├── newsletter/        # ニュースレター（将来）
│   └── social/           # SNS用コンテンツ（将来）
│
├── docs/                 # GitHub Pages用の公開HTML
│   ├── index.html
│   └── jre-point-strategy/
│       └── index.html
│
├── scripts/              # 変換スクリプトなど
│   └── convert_html_to_markdown.py
│
├── archive/              # アーカイブ（古いファイル、テストファイル）
│   ├── test/
│   └── old/
│
└── README.md             # リポジトリの説明
```

### 整理の原則

1. **`content/` が唯一の元データ**
   - すべてのコンテンツはMarkdown形式で `content/` に保存
   - Frontmatterでメタ情報を管理

2. **`docs/` は公開用HTMLのみ**
   - GitHub Pagesで公開するHTMLファイルのみ
   - `content/` から生成される（将来的には自動化）

3. **プロジェクトファイルは `archive/` または削除**
   - テストファイルは `archive/test/` へ
   - 古いファイルは `archive/old/` へ
   - または削除

4. **スクリプトは `scripts/` に集約**

## 整理手順

1. ルートのHTMLファイルを分類
2. テストファイルを `archive/test/` へ移動
3. プロジェクトファイルを適切な場所へ移動または削除
4. `content/` 構造を整備
5. `docs/` をGitHub Pages用のみに整理

