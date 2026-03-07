# Brand Style Guide
## @ino_moneycoach

**Version:** 1.0
**Date:** 2026-03-05
**Prepared for:** いの（@ino_moneycoach）

---

## 1. Brand Overview

### Brand Identity
| 項目 | 内容 |
|------|------|
| **ブランド名** | いのマネー / いのマネーニュースレター |
| **ハンドル** | @ino_moneycoach |
| **タグライン** | お得・ポイント・決済を駆使して月5万円UP |
| **ポジショニング** | 旅行×決済最適化のプロフェッショナルガイド |
| **ターゲット** | 20-40代、旅行好き、クレカ・マイル初中級者 |
| **トーン** | 知的だが親しみやすい。高級金融機関の信頼感 + 個人の温度感 |

### Brand Personality
- **Expert（専門家）**：データと根拠に基づく情報提供
- **Curator（キュレーター）**：情報の海から価値ある選択肢を厳選
- **Insider（内部者）**：「富裕層だけが知っている」情報格差を埋める存在
- **Approachable（親しみ）**：専門的だが排他的でない

---

## 2. Color Palette

### Primary Colors

| Role | Color | HEX | 用途 |
|------|-------|-----|------|
| **Brand Primary** | ティールブルー | `#14C1BD` | ロゴ、見出し、CTA、リンク、アクセント |
| **Brand Primary Light** | ライトティール | `#E8F8F8` | ハイライトボックス背景、強調エリア |
| **Text Primary** | ダークグレー | `#222222` | 見出しテキスト |
| **Text Body** | ミディアムグレー | `#333333` | 本文テキスト |

### Secondary / Neutral Colors

| Role | Color | HEX | 用途 |
|------|-------|-----|------|
| **Background** | ホワイト | `#FFFFFF` | メイン背景 |
| **Background Alt** | ライトグレー | `#F5F5F5` | 外枠背景、セクション分離 |
| **TOC Background** | ペールグレー | `#F9FAFA` | 目次、補助エリア |
| **Text Sub** | サブグレー | `#444444` | サブテキスト、キャプション |
| **Text Muted** | ミュートグレー | `#999999` | 補助テキスト、日付、注釈 |
| **Border** | ボーダーグレー | `#E5E5E7` | 区切り線、テーブル罫線 |

### Semantic Colors（データビジュアル用）

| Role | Color | HEX | 用途 |
|------|-------|-----|------|
| **Negative / 改悪** | ディープレッド | `#D32F2F` | マイナス変動、改悪表示 |
| **Negative Accent** | オレンジレッド | `#FF5722` | 数値強調（ネガティブ） |
| **Negative BG** | ライトレッド | `#FFEBEE` | ネガティブエリア背景 |
| **Positive / 改善** | ディープグリーン | `#388E3C` | プラス変動、改善表示 |
| **Positive Accent** | ブライトグリーン | `#4CAF50` | 数値強調（ポジティブ） |
| **Positive BG** | ライトグリーン | `#E8F5E9` | ポジティブエリア背景 |

### Color Usage Rules
- `#14C1BD` はブランドの顔。CTA、左ボーダー、リンクに統一使用
- 白背景（`#FFFFFF`）を基調とし、余白で高級感を演出
- セマンティックカラーはデータ比較・改悪改善表示に限定。装飾的使用は禁止
- 黒（`#000000`）は使用しない。最も濃いテキストは `#1D1D1F` or `#212121`

---

## 3. Typography

### Font Stack

```
Primary:  system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
Japanese: 'Hiragino Kaku Gothic ProN', 'メイリオ', Meiryo, sans-serif
Fallback: Helvetica Neue, Arial, sans-serif
```

### Type Scale

| Level | Size | Weight | Color | 用途 |
|-------|------|--------|-------|------|
| **Display** | 40-42pt | Bold | `#212121` | インフォグラフィックタイトル |
| **H1** | 28-36px | 600 (Semi-bold) | `#1D1D1F` | メイン見出し |
| **H2** | 20-24px | 500 (Medium) | `#1D1D1F` | セクション見出し |
| **H3** | 18-20px | 600 | `#222222` | サブセクション |
| **Body** | 16px (1rem) | 400 (Regular) | `#333333` | 本文 |
| **Small** | 13-14px | 400 | `#444444` | キャプション、サブテキスト |
| **Micro** | 11px | 400 | `#999999` | 注釈、日付 |
| **Data Number** | 22-28pt | Bold | Semantic Color | 数値データ強調 |

### Typography Rules
- line-height: 本文 `1.5`〜`1.7`、見出し `1.2`〜`1.4`
- letter-spacing: ロゴテキスト `0.05em`、タイトル `-0.5pt`
- 数値・パーセンテージは常にBold + Semantic Color
- 日本語本文はゴシック体のみ。明朝体は使用しない

---

## 4. Design Principles

### Visual Philosophy
**Apple-inspired Minimalism × Financial Authority**

1. **ホワイトスペース重視** — 余白は高級感の源泉。詰め込まない
2. **データファースト** — 装飾より数値。根拠が見える設計
3. **階層構造の明確化** — 視線の流れを設計し、重要度を視覚化
4. **モバイル最適** — すべてスマホ縦画面で完結する設計

### Layout System

| フォーマット | サイズ | 用途 |
|------------|--------|------|
| **Reels / Story** | 1080 × 1920px (9:16) | リール、ストーリーズ |
| **Feed Square** | 1080 × 1080px (1:1) | フィード投稿 |
| **Carousel** | 1080 × 1350px (4:5) | カルーセル投稿 |
| **Newsletter** | 600px固定幅 | メール配信 |

### Spacing & Radius
- border-radius: `8px`（カード、コンテナ）/ `5px`（数値バッジ）
- padding: コンテナ `2rem` / モバイル `16px`
- section間: `24px`以上
- box-shadow: `0 1px 3px rgba(0, 0, 0, 0.06)` — 控えめな影のみ

---

## 5. Component Styles

### CTA Button
```
Background: #14C1BD
Text: #FFFFFF
Border-radius: 8px
Padding: 12px 24px
Font-weight: 600
Hover: opacity 0.9
```

### Highlight Box（強調ボックス）
```
Background: #E8F8F8
Border-left: 4px solid #14C1BD
Padding: 20px
Text color: #14C1BD (見出し) / #333333 (本文)
Border-radius: 8px
```

### Table / Data Comparison
```
Header: #1D1D1F background with white text, or #F5F5F5 with dark text
Border: 1px solid #E5E5E7
Row hover: #F9FAFA
Alternating: white / #FAFAFA
改悪列: subtle #FFEBEE tint
改善列: subtle #E8F5E9 tint
```

### Newsletter Header
```
Logo text: 「いのマネーニュースレター Vol.XX」
Font-size: 13px
Letter-spacing: 0.05em
Color: #14C1BD
```

---

## 6. Voice & Tone

### Writing Style

| 属性 | 基準 | NG例 |
|------|------|------|
| **結論ファースト** | 最初の1文で要点 | 「さて、今回は…」から始める |
| **データ駆動** | 数値・比較・根拠を必ず提示 | 「すごくお得です」（定性のみ） |
| **情報格差訴求** | 「知っている人だけが得をする」構造 | 「誰でも簡単に」（安売り感） |
| **CTA表現** | 「無料で読む」「今すぐ確認する」 | 「購入はこちら」「有料noteを読む」 |
| **件名/タイトル** | 冒頭15文字にベネフィット。全体50文字以内 | 抽象的タイトル |

### Content Pillars
1. **クレジットカード** — 改悪/改善、最適解、ROI計算
2. **マイル・航空** — 特典航空券、マイル戦略、提携変更
3. **ホテル** — 上級会員攻略、コスパ最大化、裏技
4. **決済最適化** — ポイント多重取り、チャージルート、積立

### Hashtag Strategy
```
固定タグ: #クレジットカード #マイル #ポイ活 #旅行好き
テーマ別: #アメックス #ANAマイル #JALマイル #ホテル修行
フック系: #知らないと損 #お得情報 #節約術
```

---

## 7. Instagram Post Formats

### REELS（リーチ獲得）
- **冒頭3秒**: 固有名詞 × 数字で興味を引く
- **平均再生時間が最重要指標**（1秒 ≒ 1万閲覧差）
- **仮説テスト**: コスト削減訴求 vs リターン訴求のA/B
- **配分目安**: 月9本（2026年1月基準）

### FEED（資産型コンテンツ）
- **保存数がKPI**（REELSの2.5倍の保存率）
- **情報密度重視**: 1枚で完結する比較表・チェックリスト
- **配分目安**: 月8本（2026年1月基準）

### Carousel（教育・比較）
- 表紙 → 問題提起 → 解説 → 比較データ → CTA
- 最大10枚、理想は6-8枚
- 各スライドに1メッセージ

---

## 8. Do's & Don'ts

### Do's
- 白背景 + ティールアクセントの統一感を維持する
- 数値は大きく、Boldで、Semantic Colorで目立たせる
- 余白を十分に取り、Apple風のクリーン感を保つ
- モバイルファーストで視認性を検証する
- 「改悪 vs 改善」のような二項対比で情報を構造化する

### Don'ts
- 多色使い（3色以上のアクセント）で雑多な印象にしない
- 装飾的なイラスト・スタンプを多用しない
- 黒背景を使用しない（ダークモード非対応）
- 「購入はこちら」等の高圧CTAを使用しない
- 情報を詰め込みすぎない — 1投稿1メッセージの原則

---

## 9. File & Asset Locations

| 資産 | パス |
|------|------|
| NLテンプレート（HTML） | `03_NewsLetter/_template/テンプレート_いのマネーニュースレター.html` |
| NLテンプレート（MD） | `03_NewsLetter/_template/Vol10以降_改善版Markdownテンプレート.md` |
| Canva投稿素材 | `00_Projects/Canva_Posts/` |
| 画像生成プロンプト | `Gemini画像生成プロンプト_2025年クレカ衝撃ニュース早見表.md` |
| IG分析レポート | `02_Analytics/Instagram/` |
| 本ガイド | `07_Management/Brand_Style_Guide_ino_moneycoach.md` |

---

*Last updated: 2026-03-05 | v1.0*
