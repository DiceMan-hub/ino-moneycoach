---
name: newsletter-lifecycle
description: 03_NewsLetter の編集・作成・配信・アーカイブ作業を依頼されたとき、またはニュースレターの流れを確認したいときに参照する。Vol.12までの実績に基づく、ニュースレターの企画・作成・配信・配信後整理・保管までの一連のライフサイクルを Claude Code で実行する際の総合ガイド。
---

# ニュースレター ライフサイクル総括（Vol.12まで・Claude Code 用）

## 概要

このスキルは **03_NewsLetter** の「企画 → 作成 → 配信 → 配信後のデータ整理・保管」までを一括で参照するための総括です。
**Claude Code（エージェント）** がニュースレター関連のタスクを実行するとき、どの Phase で何を参照し、どのスクリプトをいつ実行するかを一覧で把握するために使います。

**適用対象:** Vol.10 以降の運用（配信チェックリスト・実行ガイドライン・ファイル管理ルールに準拠）。

---

## ライフサイクル全体像

```
Phase 1: 企画（配信3–4日前）
    ↓
Phase 2: ライティング（配信2–3日前）
    ↓
Phase 3: レビュー（配信1–2日前）
    ↓
Phase 4: 配信前最終確認（配信当日）
    ↓
配信実行（MailerLite）
    ↓
Phase 5: 配信後（翌日）→ パフォーマンス確認・改善記録・ファイル整理・保管
```

---

## Phase 1: 企画

**参照ファイル（優先順）:**

- `03_NewsLetter/Vol10_以降_配信チェックリスト.md` — Phase 1 のチェック項目
- `03_NewsLetter/Newsletter_Execution_Standard.md` — コンテンツ設計の鉄則

**やること:**

- メイン CTA を **1 つ** 決定（1 号 1 リンク）
- 読者限定要素の企画（PDF / スプレッドシート / Notion 等）
- ニュース一覧の方針（タイトルをテキストリンクに、URL なしはリンクなし）
- 段取りに「今号で参照する LINE メモ」を 2〜3 本リンクで明記（.cursorrules 準拠）

**既存スキル（必要に応じて）:**

- `.agent/skills/newsletter-planning/SKILL.md` — 企画・構成の詳細フレームワーク
- `.agent/skills/content-research/SKILL.md` — 情報収集・検証

---

## Phase 2: ライティング

**参照ファイル:**

- `03_NewsLetter/Vol10_以降_配信チェックリスト.md` — Phase 2 の全項目
- `03_NewsLetter/Newsletter_Execution_Standard.md` — 件名・プレヘッダー・ハイライト・CTA・ニュース表のルール
- `03_NewsLetter/_template/Vol10以降_改善版Markdownテンプレート.md` — ドラフトの土台（または `Vol05以降_Markdownテンプレート.md`）

**必須ルール（要約）:**

| 項目 | ルール |
|------|--------|
| 件名 | `【具体的ベネフィット】週刊マイル・ポイント通信 vol.XX`、冒頭 15 文字にベネフィット、全体 50 文字以内 |
| プレヘッダー | 件名を補足、30〜40 文字 |
| 冒頭ハイライト | 「📌 今週のハイライト」の下に **3 項目**、各「✅ 【期限・重要度】→ ベネフィット」 |
| メイン CTA | 冒頭・中盤・末尾の **3 箇所**。文言は「無料で読む」「今すぐ確認する」等 |
| ニュース表 | 「ニュース」「概要」の 2 列のみ。ニュース見出しを公式 URL のテキストリンクに（URL なしはリンクなし） |
| リンク数 | メイン CTA（3）+ Instagram + 配信停止を除き最小限、**合計 5 つ以内**が理想 |

**既存スキル（必要に応じて）:**

- `.agent/skills/newsletter-format-standardization/SKILL.md` — 表記統一
- `.agent/skills/markdown-to-html-conversion/SKILL.md` — HTML 変換

---

## Phase 3: レビュー

**参照ファイル:**

- `03_NewsLetter/Vol10_以降_配信チェックリスト.md` — Phase 3（モバイル表示・リンク数・KPI）

**確認事項:**

- Gmail アプリで件名・プレヘッダー・ファーストビューの表示
- メイン CTA 以外のリンクを最小限に
- 目標 KPI（開封率 80%、CTR 12%、CTOR 15%、解除率 0.1% 以下）

**既存スキル:**

- `.agent/skills/newsletter-consistency-check/SKILL.md` — 整合性チェック

---

## Phase 4: 配信前最終確認

**参照ファイル:**

- `03_NewsLetter/Vol10_以降_配信チェックリスト.md` — Phase 4
- 直近号の HTML: `03_NewsLetter/_archive/YYYY/VolXX_第X号/*.html` または `_working/` の当号 HTML

**確認事項:**

- ブラウザ表示・MailerLite 変数（`{$url}`, `{$unsubscribe}`）
- メイン CTA ボタンのリンク 3 箇所
- テスト送信で件名・プレヘッダー・ハイライト・CTA の動作確認

**既存スキル:**

- `.agent/skills/mailerlite-distribution-prep/SKILL.md` — 配信準備（変数・リンク・プレビュー）

---

## Phase 5: 配信後

**参照ファイル:**

- `03_NewsLetter/Vol10_以降_配信チェックリスト.md` — Phase 5（パフォーマンス確認・改善記録・**ファイル整理**）

**やること:**

1. 配信 24 時間後に開封率・CTR・CTOR・解除率を確認し、チェックリストに記録
2. 「何がうまくいったか」「次回改善点」「次号への引き継ぎ」を記録
3. **ファイル整理（必須）:** 該当号をアーカイブし、`_working` に溜めない

---

## 配信後のデータ整理・保管（Claude Code で実行する手順）

### ルール

- 該当号のファイルは **ルート** および **_working** から `_archive/YYYY/VolXX_第X号/` にまとめて移動する
- 整理は **スクリプトで実行** する。手動で移動しない（漏れ・重複を防ぐため）
- **実行前に必ず `--dry-run` で移動計画を確認する**
- `_working` に号に紐づかないファイルが残っていたら `_archive/_old/` へ移動するか削除する

### スクリプト

**パス:** `scripts/newsletter_organize.py`（リポジトリルートからの相対パス）

**実行場所:** `03_NewsLetter` から見て `../scripts/newsletter_organize.py` を呼ぶ想定。

**使用例:**

```bash
cd "/Users/mba2024/Documents/Obsidian/Dai DB/03_NewsLetter"

# 1. ドライランで移動計画を確認
python3 ../scripts/newsletter_organize.py --volume 12 --date 2026-02-21 --dry-run

# 2. 問題なければ実行（確認プロンプトあり）
python3 ../scripts/newsletter_organize.py --volume 12 --date 2026-02-21
```

**引数:**

| 引数 | 説明 |
|------|------|
| `--volume` | 号（例: `12` → Vol.12） |
| `--date` | 配信日 `YYYY-MM-DD` |
| `--dry-run` | 実際には移動せず、移動計画のみ表示 |
| `--no-confirm` | 確認プロンプトをスキップ（自動化時のみ） |
| `--list` | ルート・_working・アーカイブのファイル状況を一覧表示 |

**移動先:**

- `03_NewsLetter/_archive/YYYY/VolXX_第X号/`
- 例: `_archive/2026/Vol12_第12号/`

**移動対象（例）:**

- ルート: `YYYY_MM_DD_VolXX_いのマネーニュースレター.html`, `*_ドラフト.md`, `*_全体版_*.md` 等
- `_working`: ファイル名に `VolXX` を含む当号関連ファイル（ドラフト・チェックリスト・関連 .py 等）

**詳細ルール:**

- `03_NewsLetter/_template/ファイル管理ルール_Vol05以降.md` を参照

---

## 絶対に守る 3 つ（スキル実行時の確認）

1. **件名は新フォーマット**
   `【具体的ベネフィット】週刊マイル・ポイント通信 vol.XX`、冒頭 15 文字にベネフィット、50 文字以内

2. **1 号 1 リンク**
   メイン CTA 以外のリンクは削減。ニュース一覧は見出しを公式 URL のテキストリンクに（URL なしはリンクなし）

3. **冒頭ハイライトは必須**
   「📌 今週のハイライト」の下に 3 項目

---

## 参照ファイル一覧（Claude Code が読むべきもの）

| 用途 | パス |
|------|------|
| 配信チェックリスト（全 Phase） | `03_NewsLetter/Vol10_以降_配信チェックリスト.md` |
| 実行ガイドライン（件名・CTA・ニュース表等） | `03_NewsLetter/Newsletter_Execution_Standard.md` |
| ドラフト用テンプレート | `03_NewsLetter/_template/Vol10以降_改善版Markdownテンプレート.md` |
| ファイル管理・アーカイブルール | `03_NewsLetter/_template/ファイル管理ルール_Vol05以降.md` |
| 整理スクリプト | `scripts/newsletter_organize.py` |
| 既存スキル（企画） | `.agent/skills/newsletter-planning/SKILL.md` |
| 既存スキル（配信準備） | `.agent/skills/mailerlite-distribution-prep/SKILL.md` |
| 既存スキル（整合性チェック） | `.agent/skills/newsletter-consistency-check/SKILL.md` |

---

## ワークフロー要約（Claude Code 用）

- **企画・ドラフト作成・編集**
  → 上記 Phase 1–2 の参照ファイルと既存スキルに従い、チェックリストを満たすように編集する。
  → 関連参照候補は `.cursorrules` に従い、`LINE/processed/` 等から 2–3 本提案する。

- **HTML 変換・表記統一・整合性チェック・配信準備**
  → 該当する既存スキル（markdown-to-html-conversion, newsletter-format-standardization, newsletter-consistency-check, mailerlite-distribution-prep）を参照して実行する。

- **配信後の整理・保管**
  → `newsletter_organize.py` を `--volume` と `--date` で実行する。必ず先に `--dry-run` で確認する。
  → 整理後は `_working` に号に紐づかないファイルが残っていないか確認し、あれば `_archive/_old/` へ移動するか削除する。

これにより、Vol.12 までのやり取りで確立した「作成・配信・完了後のデータ整理と保管」までの流れを、Claude Code が一貫して参照・実行できます。
