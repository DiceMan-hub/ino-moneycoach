# Agent Skills 使用ガイド

## 📚 概要

このフォルダには、ニュースレター作成を効率化するためのAgent Skillsが含まれています。

**重要:** これらのスキルは**Vol.07〜Vol.12までの実際の作業経緯**に基づいて構築・総括されています。

## 🎯 スキル一覧

| スキル名 | 用途 | 備考 |
|---------|------|------|
| **`newsletter-lifecycle-vol12`** | **企画→作成→配信→配信後整理・保管まで一括参照** | **Claude Code 用総合ガイド（Vol.12まで総括）** |
| `newsletter-planning` | Phase 1: 企画・構成設計 | Vol.05 |
| `content-research` | Phase 2: 情報収集・検証 | Vol.05-07 |
| `markdown-to-html-conversion` | Phase 3-4: HTML変換 | Vol.07 |
| `newsletter-format-standardization` | Phase 3-4: 表記統一 | Vol.07 |
| `newsletter-consistency-check` | Phase 5: 整合性チェック | Vol.07 |
| `mailerlite-distribution-prep` | Phase 6: 配信準備 | Vol.07 |

---

## 📁 実際に存在する参考ファイル

スキルで参照しているファイルは全て実在します：

### HTMLファイル
- `03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター.html` ← **最新の実績ファイル（推奨）**
- `03_NewsLetter/_template/テンプレート_いのマネーニュースレター.html` ← 汎用テンプレート

### Markdownファイル
- `03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター_ドラフト.md`

### 作業記録
- `03_NewsLetter/_archive/2026/Vol07_第7号/作業記録_Vol07.md`
- `03_NewsLetter/_archive/2026/Vol07_第7号/README.md`

---

## 🔧 Vol.07で確立したルール（スキルに反映済み）

### 表記統一

| ルール | 内容 |
|--------|------|
| FSG表記 | 初出時「アメックスのフリーステイギフト（FSG）」、2回目以降「FSG」 |
| ホテル名 | 「ハイアット リージェンシー 瀬良垣（沖縄）」（「沖縄」を含める） |
| #PRタグ | TopCashback・Wiseに追加、マリオット・ヒルトンから削除 |
| リンク色 | **全て `#14c1bd` で統一**（赤色は使用しない） |

### CTAボタン

| 項目 | 内容 |
|------|------|
| 配置 | 2箇所（冒頭・後半） |
| 矢印 | 末尾に「→」を追加 |
| 配置 | 中央揃え |
| タイトル | 含める（長い場合は `font-size: 12px` + `line-height: 1.4`） |

### 配信準備

| 項目 | 内容 |
|------|------|
| MailerLite変数 | `{$url}`, `{$unsubscribe}` |
| note記事URL | プレースホルダーを実際のURLに置換（2箇所） |
| アーカイブ | `03_NewsLetter/_archive/2026/Vol0X_第X号/` に保存 |

---

## 🚀 使用方法

### Cursorでの使用

各Phaseで、以下のようにスキルを参照して作業を依頼します：

```
次のニュースレター（Vol.08）の企画を始めます。
.agent/skills/newsletter-planning/SKILL.md のフレームワークに従って、
配信予定日：2026年1月24日（土）18:00
で企画書を作成してください。
```

### 実際のワークフロー

**全体の流れを一括で参照する場合（Claude Code 推奨）:**

```
.agent/skills/newsletter-lifecycle-vol12/SKILL.md を読む
  → Phase に応じて参照ファイル・既存スキルをたどる
  → 配信後は scripts/newsletter_organize.py を --dry-run 後に実行
```

**Phase 別にスキルをたどる場合:**

```
1. newsletter-planning (企画)
   ↓
2. content-research (情報収集)
   ↓
3. markdown-to-html-conversion (HTML変換)
   + newsletter-format-standardization (表記統一)
   ↓
4. newsletter-consistency-check (整合性チェック)
   ↓
5. mailerlite-distribution-prep (配信準備)
   ↓
6. 配信後: newsletter-lifecycle-vol12 の「配信後のデータ整理・保管」に従い newsletter_organize.py を実行
```

---

## 💡 プロンプトのコツ

### 1. スキルファイルを明示的に参照

```
.agent/skills/[スキル名]/SKILL.md に従って...
```

### 1b. 全体の流れを一度に参照（Claude Code）

```
.agent/skills/newsletter-lifecycle-vol12/SKILL.md を読んで、
今から配信する Vol.XX の配信後整理手順を実行してほしい。
```

### 2. Vol.07の実績ファイルを参照

```
03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター.html を参考に...
```

### 3. 前のPhaseの結果を伝える

```
Phase 1の企画書が完成しました。次はPhase 2に進みます。
```

### 4. チェックリストを確認してもらう

```
.agent/skills/newsletter-consistency-check/SKILL.md の
完了チェックリストを全て確認してください。
```

---

## 📝 注意事項

1. **Vol.05/Vol.06のHTMLファイルは存在しない**
   - アーカイブにはMarkdownのみ
   - HTMLの参考は**Vol.07**を使用

2. **resourcesフォルダは空**
   - 将来的にテンプレートを追加予定
   - 現時点ではVol.07の実績ファイルを直接参照

3. **スキルの更新**
   - Vol.08以降で新しいルールが生まれたら、スキルファイルを更新する

---

## 🔗 関連ファイル

- 各スキルの詳細: `.agent/skills/[スキル名]/SKILL.md`
- 実践ガイド: `03_NewsLetter/_template/Agent_Skills_実践ガイド_Vol08から使う.md`
- テンプレート: `03_NewsLetter/_template/`
- アーカイブ: `03_NewsLetter/_archive/2026/`
