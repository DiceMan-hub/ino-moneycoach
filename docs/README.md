# GitHub Pages ファイル配置ルール

このディレクトリは GitHub Pages で公開されるコンテンツを格納します。
公開URL: https://diceman-hub.github.io/ino-moneycoach/

## 必須のディレクトリ構造

新しいHTMLページを追加する際は、**必ず**以下の構造に従ってください：

```
/docs/
  ├── project-name/
  │   └── index.html
  ├── another-project/
  │   └── index.html
  └── ...
```

## 正しい例

```
/docs/sfc-dashboard/index.html
→ URL: https://diceman-hub.github.io/ino-moneycoach/sfc-dashboard/

/docs/credit-card/index.html
→ URL: https://diceman-hub.github.io/ino-moneycoach/credit-card/
```

## 間違った例

```
/docs/sfc-dashboard.html
→ 拡張子付きURLになる（非推奨）

/docs/projects/sfc/dashboard.html
→ 深い階層は管理が複雑になる

/docs/sfc-dashboard/dashboard.html
→ /sfc-dashboard/ でアクセスできない（404になる）
```

## 新しいプロジェクトを追加する手順

1. `/docs/` 直下に新しいフォルダを作成
2. そのフォルダ内に `index.html` を配置
3. 検証スクリプトを実行: `bash scripts/validate-pages.sh`
4. コミット & プッシュ（mainブランチへ）
5. GitHub Pages が自動デプロイ（数分待つ）
6. `https://diceman-hub.github.io/ino-moneycoach/your-folder-name/` でアクセス

## Cursor / AI でプッシュする時

以下のように指示してください：

```
このHTMLファイルを GitHub Pages に公開したい。
/docs/[プロジェクト名]/index.html として配置してください。
公開前に bash scripts/validate-pages.sh を実行して検証してください。
```

## 禁止事項

- `docs/` 直下に `.html` ファイルを直接配置しない（レガシーファイルは既存のまま）
- サブフォルダを深くネストしない（1階層まで）
- `index.html` 以外のファイル名をメインファイルにしない

## 既存ファイルについて

古い構造のファイル（`.html` が直接 `/docs/` にある）は動作しているためそのまま維持しています。
新規作成時は必ず上記ルールに従ってください。
