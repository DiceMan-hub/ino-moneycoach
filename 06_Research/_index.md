# 06_Research 分類ガイド

> 最終更新: 2026-03-05

## フォルダ構造

```
06_Research/
├── _index.md              ← このファイル（分類ルール）
├── daily-intel/           ← /daily-intel skill出力
├── reddit-scan/           ← /reddit-scan skill出力
├── trend-watch/           ← /trend-watch skill出力
├── content/               ← コンテンツ企画リサーチ
├── business/              ← 外部企業分析・コンサル・事業構想
├── tech/                  ← テクノロジー・AI・セキュリティ
└── deep-research/         ← 哲学・学術的Deep Research
```

## 分類フロー

**researchとbusinessで迷いやすいので、この順番で判断する：**

```
1. skillの自動出力？
   → Yes: daily-intel/ reddit-scan/ trend-watch/（自動振分）

2. 特定の企業名・事業体が主語？
   （東京管材、税理士法人、○○社 etc.）
   → Yes: business/

3. IG投稿・note記事・NLのネタ探し？
   → Yes: content/

4. ツール・AI・セキュリティの調査？
   → Yes: tech/

5. それ以外（哲学・学術・汎用テーマ）
   → deep-research/
```

### 迷いポイント：research vs business

| 例 | 判定 | 理由 |
|---|---|---|
| 「クレカ見直しリサーチ」 | **content/** | 自分のコンテンツ企画のための調査 |
| 「東京管材_経営戦略レポート」 | **business/** | 特定企業が主語 |
| 「AI時代の哲学」 | **deep-research/** | 汎用テーマ、企業名なし |
| 「ClaudeCode機密情報リスク」 | **tech/** | ツール・セキュリティ調査 |
| 「税理士法人×AgentSkills」 | **business/** | 特定業態の事業構想 |

**判断の鍵：「特定の企業/事業体が主語か？」→ Yes = business, No = 他**

## 命名規則

```
YYYYMMDD_タイトル.md
```

- 日付は必須（ソート用）
- タイトルは内容が分かる短い日本語

## Claude Code向けメモ

- 新規リサーチファイル作成時はこの分類フローに従って配置する
- skill出力（daily-intel, reddit-scan, trend-watch）はルート直下のまま維持
- `06_BusinessKnowledge/` とは別物。06_Researchは「調べた結果」、BusinessKnowledgeは「体系化された知識」
