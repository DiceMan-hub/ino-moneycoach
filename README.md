# いのマネーコーチ コンテンツリポジトリ

このリポジトリは、いのマネーコーチのコンテンツを管理・運用するためのリポジトリです。

## 📁 ディレクトリ構造

```
/
├── content/              # VectorDB用のMarkdownコンテンツ（唯一の元データ）
│   └── guides/           # ガイド系コンテンツ
│       └── jre-point-strategy.md
│
├── docs/                 # GitHub Pages用の公開HTML
│   ├── index.html
│   └── jre-point-strategy/
│       └── index.html
│
├── scripts/              # 変換スクリプトなど
│   └── convert_html_to_markdown.py
│
└── archive/              # アーカイブ
    ├── test/             # テストファイル
    └── old/              # 古いHTMLファイル
```

## 🎯 コンテンツ管理の原則

### 1. `content/` が唯一の元データ
- すべてのコンテンツはMarkdown形式で `content/` に保存
- Frontmatterでメタ情報（id, title, date, type, tags, platforms, slug, summary, author）を管理
- VectorDBにアップロードする準備が整った形式

### 2. `docs/` は公開用HTMLのみ
- GitHub Pagesで公開するHTMLファイルのみ
- `https://diceman-hub.github.io/ino-moneycoach/` で公開
- 自動デプロイ設定済み（`.github/workflows/pages.yml`）

### 3. ファイルの整理
- テストファイル → `archive/test/`
- 古いHTMLファイル → `archive/old/`
- スクリプト → `scripts/`

## 📝 コンテンツの追加方法

1. **Markdownファイルを作成**
   - `content/guides/` または適切なディレクトリに配置
   - Frontmatterを記入

2. **GitHubにコミット・プッシュ**
   ```bash
   git add content/guides/新しいファイル.md
   git commit -m "Add new guide: タイトル"
   git push ino-moneycoach main
   ```

3. **VectorDBにアップロード**（将来的に自動化予定）

## 🔗 関連リンク

- GitHub Pages: https://diceman-hub.github.io/ino-moneycoach/
- JRE POINT戦略ガイド: https://diceman-hub.github.io/ino-moneycoach/jre-point-strategy/

## 📚 詳細

詳細な整理方針については `REPOSITORY_STRUCTURE.md` を参照してください。

