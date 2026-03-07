# Gemini CLI × Google Workspace：機密情報取り扱いリスク分析

> 作成日: 2026-03-05
> テーマ: Gemini CLIでGoogle Workspaceを利用する場合、Google Driveに機密情報を保管しているのと同レベルのリスクで運用できるか

---

## 結論：同じリスク許容度では使えない。追加リスクが存在する。

ただし、2026年3月2日リリースの `googleworkspace/cli`（gws）により、技術的懸念は大幅に緩和された。成熟度の懸念が残る。

---

## 分析対象ツールの整理

### 2つの異なるツール

| ツール | リポジトリ | 管理主体 |
|---|---|---|
| Workspace拡張（旧） | `gemini-cli-extensions/workspace` | コミュニティOSS |
| **gws（新・2026/3/2〜）** | `googleworkspace/cli` | googleworkspace org（ただし非公式サポート） |

以下の分析はgwsを中心に行う。

---

## 1. gws の概要

- Google Workspace CLI — Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin等をCLIから操作
- Google Discovery Serviceから動的にコマンドを構築（APIが増えれば自動対応）
- `gws mcp` でMCPサーバーを起動 → Claude Desktop, Gemini CLI, VS Code等から呼び出し可能
- 100+ のAIエージェントスキル内蔵
- npm配布（`npm install -g @googleworkspace/cli`）
- Apache-2.0ライセンス

---

## 2. データの取り扱い（Gemini CLI側）

| アカウント種別 | プロンプト収集 | モデル学習 |
|---|---|---|
| 個人Googleアカウント（無料） | **される** | **される可能性あり** |
| **Workspace Enterprise** | **されない** | **されない** |
| Gemini API（有料） | されない | されない |

→ Workspace Enterpriseアカウントなら学習リスクは許容範囲内

---

## 3. gws のセキュリティ機能

| 機能 | 詳細 |
|---|---|
| 認証情報の保管 | AES-256-GCM暗号化 + OS keyring |
| 認証方式 | OAuth / サービスアカウント / ドメイン全体の委任 / アクセストークン / 環境変数 |
| Model Armor | Google Cloudのプロンプトインジェクション検知・レスポンスサニタイズ統合（`--sanitize block/warn`） |
| 出力形式 | 構造化JSON（プログラム処理・フィルタリング可能） |

---

## 4. Workspace内蔵Gemini vs gws vs 旧拡張 比較

| 観点 | Workspace内蔵Gemini | gws（新） | 旧Workspace拡張 |
|---|---|---|---|
| DLP適用 | 自動適用 | Model Armorで部分対応 | 不明確 |
| 監査ログ | Admin Console一元管理 | **未確認** | 未確認 |
| CSE保護 | アクセスブロック確認済み | **未確認** | 未確認 |
| アクセス制御 | Admin Console制御 | サービスアカウント+委任対応 | OAuthトークン依存 |
| 認証情報保管 | Google管理 | AES-256-GCM+keyring | 平文リスク |
| コードベース | プロプライエタリ | OSS（googleworkspace org） | OSS（コミュニティ） |
| 公式サポート | あり | **「not officially supported」** | なし |

---

## 5. リスク分析

### データ集約リスク（最大の懸念・ツール問わず共通）

> "Gemini treats available data as usable data. What it doesn't do is evaluate business context or weigh intent."

- 権限のあるデータをAIが瞬時に集約・要約
- 過去の過剰共有設定が即座にリスクとして顕在化
- **レガシーな共有設定のミスがAIによって増幅される**

### Gemini CLI固有の脆弱性実績

| 時期 | 脆弱性 | 深刻度 |
|---|---|---|
| 2025年6-7月 | 悪意あるリポジトリで見えない任意コマンド実行 | P1/S1 |
| 2025年 | コマンド検証不備でホワイトリストバイパス | 高 |
| 2025年 | 共有ドキュメント経由のプロンプトインジェクションで企業データ窃取 | 高 |

### gws固有の懸念

1. **「not an officially supported Google product」** — 本番障害時にGoogleサポート対象外
2. **Pre-v1.0** — 「Expect breaking changes」と明記
3. **2026年3月2日作成** — セキュリティ監査・コンプライアンス認証なし
4. **監査ログの統合未確認** — Admin Consoleにgwsアクセスが記録されるか不明

### リスク評価サマリー

| リスク | 深刻度 | 対策可能性 |
|---|---|---|
| 学習へのデータ利用 | Workspace Enterpriseなら**低** | アカウント種別で制御 |
| 過去の共有設定によるデータ漏洩 | **高** | 権限棚卸し必須 |
| プロンプトインジェクション | **中**（Model Armorで緩和） | 最新版維持＋Model Armor有効化 |
| ローカル実行によるトークン漏洩 | **低〜中**（暗号化keyring） | エンドポイントセキュリティ |
| ツール成熟度 | **高** | 検証環境でのテスト |

---

## 6. 企業が取るべきアクション

1. **必ずWorkspace Enterpriseアカウントで認証**（個人アカウント厳禁）
2. **Drive全体の権限棚卸し**を先に実施
3. **最高機密ファイルにCSE適用**（全AIからのアクセスを物理的に遮断）
4. **DLP+IRMポリシー設定**（機密ラベル付きファイルへのAIアクセスをブロック）
5. **Model Armorを有効化**（`--sanitize block`）
6. **Gemini CLI・gwsは常に最新版を維持**
7. **検証環境で十分テストしてから本番導入**

---

## 7. 総合評価

| 判定軸 | 評価 |
|---|---|
| 「Drive保管と同じリスク」か？ | **No**（追加リスクあり） |
| 対策次第で許容可能か？ | **Yes**（Enterprise + CSE/DLP + 権限棚卸し前提） |
| 今すぐ本番導入すべきか？ | **No**（非公式サポート・pre-v1.0・3日前リリース） |

**技術的懸念はgwsで大幅に緩和されたが、成熟度の懸念は残る。**

---

## Sources
- [googleworkspace/cli (GitHub)](https://github.com/googleworkspace/cli)
- [gemini-cli-extensions/workspace (GitHub)](https://github.com/gemini-cli-extensions/workspace)
- [Gemini CLI: Terms of Service and Privacy Notice](https://google-gemini.github.io/gemini-cli/docs/tos-privacy.html)
- [Generative AI in Google Workspace Privacy Hub](https://support.google.com/a/answer/15706919?hl=en)
- [Gemini Enterprise Security Overview](https://docs.cloud.google.com/gemini/enterprise/docs/security-overview)
- [Is Gemini Safe? 2026 Guide](https://concentric.ai/google-gemini-security-risks/)
- [Tracebit: Gemini CLI Hijack](https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack)
- [Cyera: Gemini CLI Vulnerabilities](https://www.cyera.com/research-labs/cyera-research-labs-discloses-command-prompt-injection-vulnerabilities-in-gemini-cli)
