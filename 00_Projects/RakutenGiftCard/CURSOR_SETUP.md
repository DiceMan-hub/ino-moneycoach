# Cursorでリポジトリを開く方法

## 方法1: GitHubから直接クローン（推奨）

1. **Cursorを開く**
2. **File > Clone Repository** を選択
3. リポジトリURLを入力:
   ```
   https://github.com/DiceMan-hub/ino-moneycoach.git
   ```
4. 保存先フォルダを選択
5. 「Open」をクリック

## 方法2: コマンドラインからクローン

```bash
# リポジトリをクローン
git clone https://github.com/DiceMan-hub/ino-moneycoach.git

# Cursorで開く
cd ino-moneycoach
cursor .
```

## 方法3: Cursorで既存フォルダを開く

1. **File > Open Folder** を選択
2. 既にクローン済みの `ino-moneycoach` フォルダを選択
3. 開く

## ファイルの場所

楽天ギフトカードガイドは以下のパスにあります：
```
rakuten-gift-card-guide/rakuten_gift_card_discontinuation_guide.html
```

## その他の便利な操作

- **最新の変更を取得**: `git pull origin main`
- **変更を確認**: `git status`
- **ブランチを確認**: `git branch -a`

