# Instagram API自動化 リスク調査

- **日時**: 2026-03-01
- **形式**: Claude Code セッション
- **テーマ**: Meta Business Suite × Claude CodeでInstagram運用自動化は可能か？リスクは？

---

## 背景・きっかけ

- Meta Business Suiteのフルアクセスを取得済み
- Claude CodeでInstagramインサイト自動取得・DM対応・分析を検討

---

Meta Business Suite full access取得したんだけど、claude                              

  codeでinstagramのインサイト自動取得やDM対応・分析などはできる？                      

  

⏺ **結論：かなりできる。** Meta Business Suite（＝Instagram Graph

  API）のフルアクセスがあれば、Claude Codeから以下が実現可能。

  

  **できること**

  

  **1.** **インサイト自動取得**

  

  - **アカウントインサイト**：フォロワー推移、リーチ、インプレッション

  - **投稿別インサイト**：閲覧数、保存数、シェア、エンゲージメント

  - **リール別**：再生数、平均再生時間、リーチ

  - → 今のGoogle Spreadsheet手動運用を完全自動化できる

  

  **2.** **DM関連**

  

  - **DM受信の取得・一覧化**（Conversations API）

  - **自動返信・テンプレ送信**

  - **DM分析**（問い合わせ内容の分類・集計）

  - ※ただしMessaging APIはアプリ審査（Meta App Review）が必要

  

  **3.** **分析・レポート**

  

  - CSV不要で直接APIからデータ取得 → 分析 → Obsidianにレポート出力

  - 定期実行スクリプト化も可能

  

  **実現アプローチは2つ**

  

  **方法:** **A.** **Pythonスクリプト**

  **メリット:** シンプル、すぐ作れる

  **デメリット:** 毎回python3 xxx.py実行

  ────────────────────────────────────────

  **方法:** **B.** **MCPサーバー**

  **メリット:** Claude Codeから直接「インサイト見せて」で呼べる

  **デメリット:** 初期構築がやや手間

  

  **必要な準備**

  

  1. **Meta** **App作成**（Meta for Developersで）

  2. **アクセストークン取得**（長期トークンに変換）

  3. **Instagram** **Business** **Account** **ID**の確認

  4. DM機能を使う場合は**アプリ審査の申請**

  

  **注意点**

  

  - アクセストークンは**60日で期限切れ**（自動更新の仕組みが必要）

  - DM APIは**24時間ルール**（ユーザーからのメッセージ後24時間以内のみ返信可）

  - APIレート制限あり（1時間あたり200リクエスト程度）

## 調査結果

### 技術的に可能なこと

| 機能 | 実現手段 | 備考 |
|------|----------|------|
| アカウントインサイト取得 | Instagram Graph API | フォロワー推移、リーチ、インプレッション |
| 投稿別インサイト取得 | Instagram Graph API | 閲覧数、保存数、シェア、エンゲージメント |
| リール別データ取得 | Instagram Graph API | 再生数、平均再生時間、リーチ |
| DM受信の取得・一覧化 | Conversations API | アプリ審査（Meta App Review）が必要 |
| DM自動返信 | Messaging API | 24hルール・200通/h制限あり |
| DM分析 | API取得→Claude分析 | 問い合わせ分類・集計 |

### 実現アプローチ

| 方法 | メリット | デメリット |
|------|----------|------------|
| Pythonスクリプト | シンプル、すぐ作れる | 毎回手動実行 |
| MCPサーバー | Claude Codeから直接呼べる | 初期構築がやや手間 |

### 必要な準備

1. Meta App作成（Meta for Developers）
2. アクセストークン取得（長期トークンに変換、60日で期限切れ→自動更新必要）
3. Instagram Business Account IDの確認
4. DM機能はアプリ審査の申請が必要

---

## リスク調査

### 2025年BAN大波の事実

- 2025年5-7月に数千アカウントが一夜で停止される大規模BAN波が発生
- 原因：MetaのAIモデレーション誤判定＋非公式ツール使用者
- ビジネスアカウント・Meta Verified会員も巻き込まれた
- **公式API利用者が狙い撃ちされたわけではない**

### リスク分類

| リスクレベル | 行為 | 結果 |
|---|---|---|
| **安全** | 公式Graph APIでインサイト取得 | BANリスクなし |
| **安全** | 公式APIでDM受信の読み取り | BANリスクなし |
| **低リスク** | 公式APIでDM返信（24h以内、200通/h以下） | レート超過→1時間一時停止のみ。BANにはならない |
| **高リスク** | 非公式API・スクレイピング・モバイルエミュレーション | アカウント永久停止 |
| **高リスク** | 100いいね/h超、30フォロー/短時間 | Bot判定→停止 |

### 重要な制限事項

- 公式Graph APIでレート制限を超えてもアカウントBANにはならない（APIが1時間一時停止するだけ、2026年1月検証済み）
- 2024年10月にDMレート制限が5,000→200通/hに96%削減
- 24時間ルール：ユーザーからメッセージ受信後24時間以内のみ返信可能
- カスケード停止リスク：1アカウントがフラグされると紐づく全アカウント（個人・ビジネス・広告）が連鎖停止

### @ino_moneycoach でのリスク評価

| やりたいこと | リスク評価 |
|---|---|
| インサイト自動取得 | **ゼロ**（読み取り専用、公式API） |
| DM一覧取得・分析 | **ほぼゼロ**（読み取り専用） |
| DM自動返信 | **低**（公式API＋ルール遵守で安全） |
| フォロー/いいね自動化 | **非推奨**（Bot判定の主因） |

---

## 結論

- **公式Instagram Graph APIを使う限り、インサイト取得・DM分析は完全に安全**
- DM自動返信も公式APIでルールを守れば問題ない
- BANされるのは非公式ツール・スクレイピング利用者
- フォロー/いいね自動化はやらない

---

## 次のアクション（未決定）

- [ ] Meta App作成・トークン取得
- [ ] インサイト自動取得スクリプト or MCPサーバー構築
- [ ] 既存CSV手動運用からの移行

---

## 参考ソース

- [Instagram DM Bot Bans 2026 - SumGeniusAI](https://sumgenius.ai/blog/instagram-dm-bot-ban-wave-2026/)
- [How to Avoid Instagram Bans with DM Automation - CreatorFlow](https://creatorflow.so/blog/avoid-instagram-bans-dm-automation/)
- [Instagram Ban Wave 2025 - Medium](https://medium.com/@antiban.pro/instagram-ban-wave-2025-causes-ai-moderation-errors-and-how-to-recover-your-account-9639a063c9c2)
- [The Great Meta Ban Wave 2025 - Medium](https://medium.com/@ceo_46231/the-great-meta-ban-wave-2025-instagram-accounts-caught-in-the-crossfire-ef007135a19f)
- [Instagram API Rate Limits 2026 - CreatorFlow](https://creatorflow.so/blog/instagram-api-rate-limits-explained/)
- [Dangers of Unofficial Instagram DM APIs - Bot.space](https://www.bot.space/blog/the-dangers-of-unofficial-instagram-dm-apis-why-theyll-get-you-banned)
- [Instagram Graph API Developer Guide 2026 - Elfsight](https://elfsight.com/blog/instagram-graph-api-complete-developer-guide-for-2026/)
