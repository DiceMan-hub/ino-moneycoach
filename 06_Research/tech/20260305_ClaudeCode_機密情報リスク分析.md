# Claude Code：機密情報取り扱いリスク分析

> 作成日: 2026-03-05
> テーマ: Claude Codeを企業が機密情報を扱う環境で利用する場合のセキュリティ・プライバシーリスク
> 比較対象: Gemini CLI + gws（同日分析: `20260305_GeminiCLI_GWS_機密情報リスク分析.md`）

---

## 結論：Google Driveと同じリスク許容度では使えない

Gemini CLI以上にリスク差が大きい。根本的な構造差として「データが推論のためにAnthropicの米国サーバーに送信される」点がGoogle Drive（保存はGoogleインフラ内完結）と異なる。

---

## 1. データ取り扱い

### 1-1. モデル学習への利用

| プラン                          | 学習利用                 | 制御方法                |
| ---------------------------- | -------------------- | ------------------- |
| Free / Pro / Max（個人）         | **設定ONの場合、学習に使用される** | Privacy設定でON/OFF切替可 |
| **Team / Enterprise**        | **不使用保証**            | デフォルトで不使用           |
| **API（直接キー利用）**              | **不使用保証**            | Commercial Terms適用  |
| Bedrock / Vertex / Foundry経由 | **不使用保証**            | 各クラウドプロバイダー規約適用     |

**注意**: 2025年10月のConsumer Terms改定により、Free/Pro/Maxはデフォルトで学習利用ON。

### 1-2. データ保持期間

| 条件 | 保持期間 |
|------|----------|
| Consumer（学習利用ON） | **5年間** |
| Consumer（学習利用OFF） | **30日間** |
| Team / Enterprise（標準） | **30日間** |
| **Enterprise（ZDR有効化時）** | **即時削除** |
| `/bug`コマンド経由のフィードバック | **5年間** |

**ZDR（Zero Data Retention）の例外**: 利用規約違反フラグ時は最大2年間保持の可能性あり。

### 1-3. データ処理リージョン

- **データ保存先**: 米国（変更不可）
- **推論処理**: 米国・欧州・アジア・豪州に分散ルーティング
- インフラ基盤: AWS
- **日本リージョン保証: なし**

---

## 2. MCP経由でGoogle Workspaceに接続した場合

### 2-1. データフロー

```
ユーザー → Claude Code（ローカル） → MCPサーバー（ローカル） → Google API
                ↓
         Anthropic API（推論・米国）
```

- MCPサーバーはローカルで実行されるが、**取得したデータはAnthropicの推論APIに送信される**
- MCPサーバーは認証トークンを保持 → 「鍵束を一括で奪われる」リスク

### 2-2. Google DLP/CSEの適用状況

| 保護機能 | MCP経由での適用 |
|----------|----------------|
| Google CSE | **有効**（CSE対象ファイルはMCP経由でも読めない） |
| Google DLP | **バイパスされる可能性あり**（APIに直接アクセスするため） |
| Google IRM | 未検証 |

### 2-3. MCPサーバーの重大な制約

- **AnthropicはMCPサーバーを一切管理・監査していない**（公式ドキュメント明記）
- MCPサーバーはフルシステム権限で動作可能
- ツールチェーニング攻撃（低信頼コネクタ→高信頼エグゼキュータ）に対するハードコードされた保護がない

---

## 3. エンタープライズセキュリティ機能

### 3-1. プラン別機能比較

| 機能 | Free/Pro/Max | Team | Enterprise |
|------|-------------|------|-----------|
| 学習不使用保証 | 設定次第 | **保証** | **保証** |
| ZDR（即時削除） | 不可 | 不可 | **可能** |
| SSO（SAML/OIDC） | 不可 | 不可 | **可能** |
| Managed Policy | 不可 | 一部 | **完全対応** |
| 監査ログ | 不可 | 一部 | **完全対応** |
| Compliance API | 不可 | 不可 | **可能** |

### 3-2. コンプライアンス認証

| 認証 | 状態 |
|------|------|
| SOC 2 Type II | 取得済み |
| ISO 27001 | 取得済み |
| HIPAA | 対応（BAA締結可能） |
| GDPR | 対応 |
| BYOK | **2026年H1予定** |

---

## 4. Claude Code固有の脆弱性実績

### CVE-2025-59536（CVSS 8.7）
- Hooks・MCPサーバー・環境変数を悪用し、リポジトリ設定ファイルから**任意コード実行**
- 悪意あるリポジトリをclone→Claude Code起動するだけでRCE

### CVE-2026-21852
- ユーザー操作なしで**APIキーを窃取可能**
- MCPサーバーがユーザー承認前に実行可能だった

### DXT拡張機能のゼロクリックRCE（CVSS 10.0）
- Googleカレンダー予定にペイロード → Claude Desktop経由でRCE
- 10,000人以上に影響
- **Anthropicは「MCPの意図した設計と一致する」として修正しない方針**（報道ベース）

### プロンプトインジェクション対策（実装済み）
- 権限システム（機密操作は明示的承認必須）
- コマンドブロックリスト（curl, wgetはデフォルト禁止）
- WebFetchの隔離コンテキスト
- コマンドインジェクション検出
- ただし公式が「完全な免疫はない」と明記

---

## 5. Gemini CLI + gws との比較

| 観点 | Claude Code | Gemini CLI + gws |
|------|------------|------------------|
| データ学習ポリシー | Enterprise/APIは不使用保証 | Workspace Enterpriseは不使用保証 |
| ZDR | Enterprise + APIで利用可能 | Vertex AI経由で利用可能 |
| **データ保存リージョン** | **米国固定** | GCPリージョン選択可能 |
| **GWS統合** | **MCP経由（非公式）** | **ネイティブ統合** |
| **Google DLP互換性** | バイパスされる可能性あり | **ネイティブ適用** |
| **コンプライアンス認証** | SOC 2, ISO 27001 | **SOC 1/2/3, ISO 27001/27017/27018/27701**（より広範） |
| **ネットワーク制御** | VPN対応、サンドボックス | **VPC Service Controls, Private Google Access** |
| オープンソース | CLI部分は公開（コア非公開） | **Apache 2.0完全OSS** |
| **脆弱性実績** | **CVSS 8.7-10.0が複数** | P1/S1が複数（いずれも修正済み） |
| MCPサーバー管理 | **Anthropic未監査** | Model Armor統合 |

### Gemini CLIの優位点（GWS連携用途）
- Google Workspaceとのネイティブ統合（DLP/CSEが自然に効く）
- VPC Service Controlsによるネットワーク境界制御
- データがGoogleエコシステム内で完結

### Claude Codeの優位点
- コーディング能力の評価が一般的に高い
- ZDRがCLI利用に直接適用可能
- Managed Policyによる組織レベルの権限強制

---

## 6. Google Driveとのリスク比較

| 観点 | Google Drive | Claude Code |
|------|-------------|------------|
| データ保存先の管理 | リージョン選択可能。CSEで自社鍵暗号化 | **米国固定。BYOK未対応（2026H1予定）** |
| データ学習リスク | Workspace版は不使用保証 | Enterprise/APIなら不使用だが**プラン選択ミスで5年保持** |
| DLP | 組織全体のDLPルール適用 | **DLP機能は未成熟** |
| アクセス制御の粒度 | ファイル/フォルダ/ユーザー/グループ単位 | 起動ディレクトリ単位。ファイル単位の制御なし |
| 脆弱性実績 | 20年以上の運用実績 | **CVSS 8.7-10.0の脆弱性が2025-2026年に複数** |
| サードパーティリスク | Google自身が管理 | **MCPサーバーはAnthropicが未監査** |
| 監査の成熟度 | 包括的な監査ログ、eDiscovery対応 | 監査ログ30日保持。eDiscovery未対応 |

---

## 7. リスクを許容可能にするための条件

以下の**全て**を満たす場合に限り、リスクを許容可能に近づけられる:

1. **Enterpriseプラン**を利用（Team不可。Free/Pro/Maxは論外）
2. **ZDR（Zero Data Retention）を有効化**
3. **Managed Policyで組織全体の権限を統制**
4. **MCPサーバーは自社開発 or 厳格に監査されたもののみ使用**
5. **サンドボックスを有効化**
6. **Bedrock / Vertex経由で利用**（非必須テレメトリを全無効化）
7. **信頼できないリポジトリでClaude Codeを実行しない**運用ルール
8. **Google Drive接続はCSE有効ファイルに限定**
9. **2026年H1のBYOK対応**を待ってから本格導入

---

## 8. 実務的な推奨

1. **機密度の低いコード**（OSS、公開予定のコード）から段階的に導入
2. **機密情報は環境変数・シークレット管理ツールに分離**し、Claude Codeからアクセスできない構成にする
3. **Google Workspaceの機密ファイルにはCSEを適用**（MCP経由でも読めない状態にする）
4. **Google Workspace統合用途ではGemini CLI + Gemini Code Assist Enterpriseを併用検討**（DLP/CSEがネイティブに効く）
5. **脆弱性情報を定期監視**: Anthropic HackerOne、GitHub Issues
6. **2026年H1のBYOK対応**を待ってから本格的な機密データ利用を検討

---

## 情報の不確実性

- Anthropicの製品・ポリシーは急速に変化しており、本レポートの情報は2026年3月時点のもの
- DXT脆弱性に対する「修正しない方針」は報道ベースであり、Anthropicの公式声明を直接確認できていない
- 一部の情報源は公式ドキュメントの二次情報

---

## Sources

- [Claude Code Data Usage公式ドキュメント](https://code.claude.com/docs/en/data-usage)
- [Claude Code Security公式ドキュメント](https://code.claude.com/docs/en/security)
- [Claude Code Zero Data Retention](https://code.claude.com/docs/en/zero-data-retention)
- [Anthropic Privacy Center](https://privacy.claude.com/)
- [Anthropic Trust Center](https://trust.anthropic.com)
- [Check Point Research - CVE-2025-59536 / CVE-2026-21852](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)
- [The Hacker News - Claude Code Flaws](https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html)
- [Infosecurity Magazine - Zero-Click Flaw in Claude Extensions](https://www.infosecurity-magazine.com/news/zeroclick-flaw-claude-dxt/)
- [Pillar Security - MCP Security Risks](https://www.pillar.security/blog/the-security-risks-of-model-context-protocol-mcp)
- [Red Hat - MCP Security Risks and Controls](https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls)
- [Google Cloud - MCP Security Framework](https://medium.com/google-cloud/google-clouds-mcp-security-framework-explained-your-ai-agent-shouldn-t-have-more-access-than-it-900af267b7bd)
- [Anthropic - Claude Code and new admin controls](https://www.anthropic.com/news/claude-code-on-team-and-enterprise)
- [Claude Help Center - Audit Logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs)
- [Shipyard - Claude Code vs Gemini CLI](https://shipyard.build/blog/claude-code-vs-gemini-cli/)
