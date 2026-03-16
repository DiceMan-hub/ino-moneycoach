# GitHub Pages ファイル配置ルール

このディレクトリは GitHub Pages で公開されるコンテンツを格納します。

## 📁 必須のディレクトリ構造

新しいHTMLページを追加する際は、**必ず**以下の構造に従ってください：

```
/docs/
  ├── project-name/
  │   └── index.html
  ├── another-project/
  │   └── index.html
  └── ...
```

## ✅ 正しい例

```bash
# ✅ 正しい - /sfc-dashboard/ でアクセス可能
/docs/sfc-dashboard/index.html
→ URL: https://diceman-hub.github.io/ino-moneycoach/sfc-dashboard/

# ✅ 正しい - /credit-card/ でアクセス可能
/docs/credit-card/index.html
→ URL: https://diceman-hub.github.io/ino-moneycoach/credit-card/
```

## ❌ 間違った例

```bash
# ❌ 間違い - 拡張子付きURLになる
/docs/sfc-dashboard.html
→ URL: https://diceman-hub.github.io/ino-moneycoach/sfc-dashboard.html

# ❌ 間違い - 深い階層は避ける
/docs/projects/sfc/dashboard.html
→ 管理が複雑になる

# ❌ 間違い - ファイル名が index.html 以外
/docs/sfc-dashboard/dashboard.html
→ /sfc-dashboard/ でアクセスできない
```

## 📝 新しいプロジェクトを追加する手順

1. `/docs/` 直下に新しいフォルダを作成
2. 2. そのフォルダ内に `index.html` を配置
   3. 3. コミット＆プッシュ
      4. 4. GitHub Pages が自動デプロイ（数分待つ）
         5. 5. `https://diceman-hub.github.io/ino-moneycoach/your-folder-name/` でアクセス
           
            6. ## 🔧 Cursor / Antigravity でプッシュする時
           
            7. 以下のコマンドをAIに指示してください：
           
            8. ```
               このHTMLファイルを GitHub Pages に公開したい。
               /docs/[プロジェクト名]/index.html として配置してください。
               ```

               ## 🚫 禁止事項

               - `docs` 直下に `.html` ファイルを直接配置しない
               - - サブフォルダを深くネストしない（1階層まで）
                 - - `index.html` 以外のファイル名をメインファイルにしない
                  
                   - ## 📌 既存ファイルについて
                  
                   - 古い構造のファイル（`.html` が直接 `/docs/` にある）は段階的に移行予定です。
                   - 新規作成時は必ず上記ルールに従ってください。
