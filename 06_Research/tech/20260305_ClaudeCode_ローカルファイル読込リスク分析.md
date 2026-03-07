# Claude Code ローカルMarkdownファイル読み込み時のセキュリティ・プライバシーリスク分析

> 作成日: 2026-03-05
> テーマ: Claude CodeでローカルのMarkdownファイルを読み込ませて作業する場合の安全性
> 前提: Google Workspace等の外部サービスには接続しない
> 関連レポート: `20260305_ClaudeCode_機密情報リスク分析.md`

---

## 結論

**ローカルファイルの読み込みは「ローカル完結」ではない。**
Readツールで読んだファイル内容は**全てAnthropicのAPIに送信される**。ローカル処理の選択肢はない。

ただし、MCP経由のGWS接続と比べるとリスクは限定的。プラン選択と設定次第で「中程度の機密情報」までは実用的に使える。

---

## 1. データフロー：ファイル内容は必ずAnthropicに送信される

公式ドキュメント（Data usage - Claude Code Docs）より：

> Claude Code runs locally. In order to interact with the LLM, Claude Code sends data over the network. This data includes **all user prompts and model outputs**. The data is encrypted in transit via TLS and **is not encrypted at rest**.

| 経路 | 暗号化 | 備考 |
|------|--------|------|
| ローカル → Anthropic API | **TLS暗号化あり** | 転送中は保護される |
| Anthropic側での保存 | **暗号化なし** | "not encrypted at rest" |
| テレメトリ（Statsig/Sentry） | 送信あり | コードやファイルパスは含まれない |

### ファイル内容がローカルに留まるケースはない

Readツールの出力はAPIリクエストのペイロードに含まれる。唯一の例外はサンドボックスやパーミッション拒否ルールで**読み取り自体がブロック**された場合（=そもそも読まない）。

### コンテキスト圧縮時の扱い

- 50K文字超のツール結果はローカルディスクに永続化される
- 圧縮処理自体もAPI側で行われるため、**圧縮前のデータはAPIに送信済み**

---

## 2. プラン別のデータ保護レベル

| プラン | 学習利用 | 保持期間 | ローカルMD読み込み時の安全度 |
|--------|----------|----------|--------------------------|
| Free/Pro/Max | **デフォルトON** | ON: 5年 / OFF: 30日 | **低**（オプトアウト必須） |
| Team | OFF | 30日 | **中** |
| Enterprise | OFF | 30日 / ZDR可 | **高** |
| API Key直接利用 | OFF | 7日（2025/9/15〜） | **中〜高** |
| Bedrock/Vertex | OFF | AWS/GCP規約準拠 | **高**（テレメトリも全OFF） |

### ZDR（Zero Data Retention）

- Enterprise限定
- プロンプトとモデル応答はリアルタイム処理後、Anthropic側に保存されない
- 例外：利用規約違反フラグ時は最大2年保持
- **機密ファイルを読ませるなら最も安全な選択肢**

---

## 3. ローカル読み込み固有のリスク

### 3-1. 意図しないファイルの読み込み（重大）

公式ドキュメント（Security - Claude Code Docs）：

> Claude Code can only **write** to the folder where it was started and its subfolders. While Claude Code **can read files outside the working directory**, write operations are strictly confined to the project scope.

- **読み取り**: システム全体にアクセス可能（デフォルト）
- **書き込み**: 作業ディレクトリ＋サブのみ
- 別ディレクトリでClaude Codeを起動しても、Obsidianのファイルが読まれる可能性がある

### 3-2. .envファイルの自動読み込み問題

Knostic社の報告：
- Claude Codeは`.env`、`.env.local`等を**ユーザーに通知せずに自動読み込み**
- `.claudeignore`や`.gitignore`に記載していても**無視されるケース**あり
- APIキー、トークン、パスワードが意図せずメモリにロードされる

### 3-3. CLAUDE.md経由のプロンプトインジェクション

CVE-2025-59536（修正済み）：
- `.claude/settings.json`のHooks機能を悪用し、セッション開始時に任意コマンド実行
- 悪意あるリポジトリをcloneするだけで**ユーザーが確認する前に**コマンドが実行

### 3-4. パーミッション拒否ルールの不完全性

GitHub Issue #6631で報告：
- denyルールがRead/Writeツールに対して**機能しないバグ**（2025年8月）
- `diff`コマンド経由で拒否されたファイルを読む回避策も発見
- v2.0.22で改善されたが**完全な信頼は置けない**

### 3-5. ファイルパスの漏洩

- テレメトリにはファイルパスは含まれない（公式記載）
- ただし**APIに送信されるプロンプト内にはファイルパスが含まれる**（Readツールの引数）
- `/bug`コマンド使用時は**会話全体（ファイルパス含む）が5年間保持**

---

## 4. サンドボックス・権限モデル

### macOS Seatbeltサンドボックス

- `/sandbox`コマンドで有効化（追加インストール不要）
- **ファイルシステム隔離**: 作業ディレクトリへの読み書きのみ許可
- **ネットワーク隔離**: 承認済みドメインのみ接続可能
- OS level強制 → 子プロセスにも継承
- Anthropicベンチマーク：攻撃面を**95%削減**

### サンドボックスの限界

- ネットワーク：ドメインレベルの制限のみ（内容は検査しない）
- ドメインフロンティング：広範ドメイン許可時のデータ窃取リスク
- Unixソケット：Dockerソケット等でバイパス可能
- `--dangerously-skip-permissions`で全保護が無効化される

---

## 5. ローカル完全処理の代替手段

| 選択肢 | 概要 | 実用性 |
|--------|------|--------|
| Devstral 2（Mistral AI） | エージェントコーディング特化OSS | Claude比で劣るが実用的 |
| Llama 3-70B | ローカル実行可能 | ナレッジ管理には十分 |
| Qwen 2.5-72B | 高性能OSS | 日本語対応は限定的 |

**Claude Codeと同等のエージェント機能をローカルで再現するのは現時点で困難。**

### Bedrock/Vertex経由での改善

| 項目 | Claude API（直接） | Bedrock/Vertex |
|------|-------------------|----------------|
| Statsigテレメトリ | デフォルトON | **デフォルトOFF** |
| Sentryエラー報告 | デフォルトON | **デフォルトOFF** |
| /bugレポート | デフォルトON | **デフォルトOFF** |
| 学習利用 | プラン依存 | **完全OFF** |
| データ処理主体 | Anthropic | **AWS/GCP** |

---

## 6. 実務的な対策

### 即座に実行すべき設定

**a) 学習利用のオプトアウト（Free/Pro/Maxの場合）**

claude.ai/settings/data-privacy-controls でモデル改善への利用をOFFにする。

**b) テレメトリの一括無効化**

```bash
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1
```

**c) サンドボックスの有効化**

Claude Code内で `/sandbox` を実行。

**d) 機密ファイルの読み取り拒否設定**

`~/.claude/settings.json`:
```json
{
  "permissions": {
    "deny": [
      "Read(./.env*)",
      "Read(./secrets/**)",
      "Read(./**/credentials*)"
    ]
  }
}
```

### ディレクトリ構造の工夫

```
~/Documents/
├── Obsidian/Dai DB/       ← 機密度：中（分析・戦略）
│   ├── 00_Projects/       ← Claude Codeに読ませてOK
│   ├── 02_Analytics/      ← Claude Codeに読ませてOK
│   ├── 07_Management/     ← 事業計画→慎重判断
│   └── _CONFIDENTIAL/     ← 顧客情報→読ませない
├── _NO_AI/                ← Claude Codeを絶対起動しないディレクトリ
│   ├── 顧客リスト/
│   ├── 契約書/
│   └── 確定申告/
└── Work/                  ← Claude Code作業ディレクトリ
```

### 機密レベル別の許容度判断

| 機密レベル | 具体例 | Claude Code使用 | 推奨プラン・対策 |
|-----------|--------|----------------|----------------|
| **低** | 公開済みnote記事、一般的な投稿ネタ | **OK** | 特になし |
| **中** | 事業戦略、売上分析、投稿パフォーマンス | **条件付きOK** | オプトアウト必須、API Key（7日保持）推奨 |
| **高** | 顧客のメールアドレス・DM内容 | **非推奨** | Enterprise ZDR、またはローカルLLM |
| **最高** | 確定申告データ、マイナンバー、口座情報、契約書 | **禁止** | AI処理自体を避ける |

### その他のベストプラクティス

1. **Claude Codeを常に最新版に維持**（CVE修正の即時適用）
2. **信頼できないリポジトリでClaude Codeを起動しない**
3. **`/bug`コマンドは機密データ使用中に実行しない**（会話全体が5年間保持）
4. **`--dangerously-skip-permissions`は機密環境下で絶対に使わない**
5. **devcontainer（Docker）でファイルシステム隔離を強化**

---

## GWS接続ありの場合との比較

| 観点 | ローカルMDのみ | MCP経由GWS接続 |
|------|--------------|----------------|
| データ送信先 | Anthropic APIのみ | Anthropic API + Google API |
| 攻撃面 | Claude Code本体のみ | + MCPサーバー + OAuthトークン |
| DLPバイパス | 関係なし | バイパスリスクあり |
| サードパーティリスク | なし | MCPサーバーの信頼性依存 |
| データ集約リスク | 指定したファイルのみ | Google全体が検索対象 |

**→ ローカルMDのみの方が明確にリスクが低い。**

---

## Sources

- [Data usage - Claude Code Docs](https://code.claude.com/docs/en/data-usage)
- [Security - Claude Code Docs](https://code.claude.com/docs/en/security)
- [Sandboxing - Claude Code Docs](https://code.claude.com/docs/en/sandboxing)
- [Zero data retention - Claude Code Docs](https://code.claude.com/docs/en/zero-data-retention)
- [Anthropic Privacy Center](https://privacy.claude.com/)
- [Claude Code Automatically Loads .env Secrets | Knostic](https://www.knostic.ai/blog/claude-loads-secrets-without-permission)
- [CVE-2025-59536 | Check Point Research](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)
- [Permission Deny Bug | GitHub Issue #6631](https://github.com/anthropics/claude-code/issues/6631)
- [Claude Code Sandboxing | Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-sandboxing)
- [Claude Code Security Best Practices | Backslash](https://www.backslash.security/blog/claude-code-security-best-practices)
