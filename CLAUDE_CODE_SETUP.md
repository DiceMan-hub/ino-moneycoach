# Claude Code拡張機能セットアップガイド

## 概要

このワークスペースでClaude Code拡張機能を使用するための環境設定です。

## セットアップ手順

### 1. 拡張機能のインストール

CursorまたはVS Codeを開き、以下の拡張機能をインストールしてください：

#### 必須拡張機能
- **Anthropic Claude Code** - Claude AIとの統合

#### 推奨拡張機能
- **Python** - Python言語サポート
- **Pylance** - Python型チェックとインテリセンス
- **ESLint** - JavaScript/TypeScriptのリント
- **Prettier** - コードフォーマッター
- **TypeScript and JavaScript Language Features** - TypeScript/JavaScriptサポート
- **Live Server** - HTMLファイルのライブプレビュー

### 2. 拡張機能のインストール方法

#### 方法1: 自動インストール（推奨）
1. Cursor/VS Codeを開く
2. ワークスペースを開くと、拡張機能のインストールを促す通知が表示されます
3. 「Install」をクリック

#### 方法2: 手動インストール
1. `Cmd+Shift+P` (Mac) または `Ctrl+Shift+P` (Windows/Linux) でコマンドパレットを開く
2. "Extensions: Show Recommended Extensions" を実行
3. 各拡張機能の「Install」をクリック

### 3. Claude APIキーの設定

Claude Code拡張機能を使用するには、Anthropic APIキーが必要です：

1. [Anthropic Console](https://console.anthropic.com/) にアクセス
2. APIキーを取得
3. Cursor/VS Codeの設定でAPIキーを設定：
   - `Cmd+,` (Mac) または `Ctrl+,` (Windows/Linux) で設定を開く
   - "Claude" を検索
   - APIキーを入力

または、環境変数として設定：
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 4. ワークスペース設定の確認

`.vscode/settings.json` に以下の設定が含まれています：
- 自動フォーマット（保存時）
- HTML/JavaScript/TypeScript/Pythonのフォーマッター設定
- ファイルエンコーディング（UTF-8）
- その他の開発環境設定

### 5. 使用方法

#### Claude Code拡張機能の基本操作
1. **コード補完**: コードを入力すると、Claudeが自動的に候補を提案します
2. **コード生成**: `Cmd+I` (Mac) または `Ctrl+I` (Windows/Linux) でインライン補完をリクエスト
3. **チャット**: サイドバーからClaudeチャットを開いて質問やコードレビューを依頼

#### HTMLファイルの開発
- **Live Server**: HTMLファイルを右クリック → "Open with Live Server" でブラウザでプレビュー
- ファイルを保存すると自動的にブラウザが更新されます

## トラブルシューティング

### 拡張機能がインストールされない場合
- Cursor/VS Codeを再起動してください
- 拡張機能のバージョンが最新か確認してください

### Claude APIが動作しない場合
- APIキーが正しく設定されているか確認してください
- インターネット接続を確認してください
- Anthropic ConsoleでAPIキーの有効性を確認してください

### フォーマットが動作しない場合
- Prettierがインストールされているか確認してください
- 設定ファイル（`.vscode/settings.json`）が正しく読み込まれているか確認してください

## 参考リンク

- [Anthropic Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code)
- [Anthropic API Documentation](https://docs.anthropic.com/)
- [Cursor Documentation](https://cursor.sh/docs)

