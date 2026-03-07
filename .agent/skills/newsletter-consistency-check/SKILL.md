---
name: Newsletter Consistency Check
description: HTMLとMarkdownファイルの整合性を検証するスキル。Vol.07の実績に基づき、タイトル、CTAボタン、表記、リンクなど、全ての要素が一致していることを確認します。
---

# Newsletter Consistency Check Skill

## 🎯 概要

このスキルは、ニュースレター作成の**Phase 5: 品質保証**をサポートします。

**使用タイミング:**

- HTML変換が完了した後
- 配信前の最終チェック時
- 表記やリンクを修正した後

**所要時間目安:** 約 15 分（手動）→ 自動化により 1-2 分に短縮可能

**前提スキル:** `markdown-to-html-conversion` でHTML変換が完了していること

---

## 📋 整合性チェックフレームワーク（Vol.07実績ベース）

### Step 1: タイトル・メタ情報の確認（3 分）

#### チェック項目

- [ ] **HTMLの`<title>`タグ** = Markdownの「件名案」
- [ ] **HTMLのh1タグ** = Markdownの「# タイトル」
- [ ] **配信日** = 両方で一致
- [ ] **プレヘッダー** = 両方で一致

#### 検証方法

```bash
# HTMLからタイトルを抽出
grep -o '<title>.*</title>' newsletter.html

# Markdownから件名を抽出
grep '件名案：' newsletter.md
```

---

### Step 2: CTAボタンの確認（5 分）

**Vol.07で確立した2箇所のCTAボタン:**

#### チェック項目

- [ ] **冒頭のCTAボタン** = Markdownの冒頭リンク
- [ ] **後半のCTAボタン** = Markdownの後半リンク
- [ ] **ボタンのテキスト** = 両方で一致
- [ ] **リンクURL** = 両方で一致（プレースホルダーでないこと）
- [ ] **矢印（→）** = 両方に含まれている

#### 検証方法

**HTML:**
```html
<!-- 冒頭CTA -->
<a href="https://bit.ly/XXXXXXX">タイトル →</a>

<!-- 後半CTA -->
<a href="https://bit.ly/XXXXXXX">タイトル →</a>
```

**Markdown:**
```markdown
**[タイトル →](https://bit.ly/XXXXXXX)**
```

**重要:** `note記事URL` などのプレースホルダーが残っていないか確認

---

### Step 3: 表記の統一確認（5 分）

#### FSG表記（Vol.07で確立）

- [ ] **初出時**: 「アメックスのフリーステイギフト（FSG）」
- [ ] **2回目以降**: 「FSG」または「FSG（アメックスのフリーステイギフト）」
- [ ] HTMLとMarkdownで同じ表記を使用

#### ホテル名（Vol.07で確立）

- [ ] **統一表記**: 「ハイアット リージェンシー 瀬良垣（沖縄）」
- [ ] タイトル、ハイライト、CTAボタン、目次で一致
- [ ] 本文中の表記も統一

#### #PRタグ（Vol.07で確立）

- [ ] **対象サービス**: TopCashback、Wise
- [ ] **非対象**: マリオット、ヒルトン（Vol.07以降）
- [ ] HTMLとMarkdownで同じ配置

#### リンク色（Vol.07で修正）

- [ ] **全てのリンクが `#14c1bd`**
- [ ] **赤色リンク（`#e53935`等）がないこと**

#### 検証方法

```bash
# FSG表記の確認
grep -i "FSG\|フリーステイギフト" newsletter.html newsletter.md

# ホテル名の確認
grep -i "ハイアット.*瀬良垣" newsletter.html newsletter.md

# #PRタグの確認
grep "#PR" newsletter.html newsletter.md

# 赤色リンクの確認（あってはいけない）
grep -i "color.*#e53935\|color.*red" newsletter.html
```

---

### Step 4: リンクURLの確認（2 分）

#### チェック項目

- [ ] **note記事URL**: プレースホルダー（`note記事URL`）が実際のURLに置き換えられている
- [ ] **外部リンク**: 全てのリンクが有効
- [ ] **MailerLite変数**: `{$url}`, `{$unsubscribe}` が設定されている

#### 検証方法

```bash
# プレースホルダーの確認（あってはいけない）
grep "note記事URL" newsletter.html

# MailerLite変数の確認（あるべき）
grep "{\$url}" newsletter.html
grep "{\$unsubscribe}" newsletter.html
```

---

### Step 5: コンテンツの一致確認（5 分）

#### チェック項目

- [ ] **セクション構成**: HTMLとMarkdownで同じセクション順序
- [ ] **ニュースアイテム**: 全てのニュースが両方に含まれている
- [ ] **テキスト内容**: 主要な文章が一致している
- [ ] **数値・日付**: 金額、日付、パーセンテージが一致

#### 検証方法

**セクション構成の確認:**
```bash
# HTMLのセクション
grep -E "<h2|<h3" newsletter.html

# Markdownのセクション
grep -E "^##|^###" newsletter.md
```

**ニュースアイテムの確認:**
```bash
# HTMLのニュース
grep -A 2 "サービス" newsletter.html | grep "<a href"

# Markdownのニュース
grep "^\|.*\[.*\](http" newsletter.md
```

---

## 🔍 詳細チェックリスト（Vol.07実績ベース）

### タイトル関連

- [ ] HTML `<title>` = Markdown 件名案
- [ ] HTML h1 = Markdown # タイトル
- [ ] HTML プレヘッダー = Markdown 配信日時

### CTAボタン（Vol.07で2箇所に）

- [ ] 冒頭CTA: テキスト一致
- [ ] 冒頭CTA: URL一致
- [ ] 後半CTA: テキスト一致
- [ ] 後半CTA: URL一致
- [ ] 両方に矢印（→）が含まれている
- [ ] 両方が中央揃えになっている

### 表記統一（Vol.07で確立）

- [ ] FSG表記が統一されている
- [ ] ホテル名が統一されている（「沖縄」を含む）
- [ ] #PRタグの配置が一致している
- [ ] **リンク色が `#14c1bd` で統一されている**

### リンク

- [ ] note記事URLが実際のURLに置き換えられている
- [ ] 全ての外部リンクが有効
- [ ] MailerLite変数が設定されている

### コンテンツ

- [ ] セクション構成が一致
- [ ] ニュースアイテムが全て含まれている
- [ ] 主要なテキストが一致
- [ ] 数値・日付が一致

---

## ✅ 完了チェックリスト

整合性チェック完了時に以下を確認：

- [ ] タイトル・メタ情報が一致している
- [ ] CTAボタンが2箇所とも一致している
- [ ] 表記（FSG、ホテル名、#PR、リンク色）が統一されている
- [ ] リンクURLが正しく設定されている
- [ ] コンテンツの主要部分が一致している
- [ ] 不一致が見つかった場合、両方のファイルを修正した

---

## 📚 参考資料

**実際に存在するファイル:**
- `03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター.html` - Vol.07の実績HTMLファイル
- `03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター_ドラフト.md` - Vol.07のMarkdownドラフト
- `03_NewsLetter/_archive/2026/Vol07_第7号/作業記録_Vol07.md` - Vol.07の作業記録

---

## 🔗 次のスキル

整合性チェック完了後は、以下のスキルに進む：

1. **newsletter-format-standardization** - 表記の統一確認（必要に応じて）
2. **mailerlite-distribution-prep** - 配信準備

---

## 💡 Vol.07で学んだ教訓

1. **HTMLとMarkdownの整合性**: 両方のファイルを同時に修正しないと、不一致が発生する
2. **CTAボタンの2箇所**: 冒頭と後半の両方を確認する必要がある
3. **プレースホルダーの確認**: `note記事URL` が残っていると配信時にリンク切れになる
4. **リンク色の確認**: 赤色リンクが混在していないか確認する
5. **表記の統一**: FSG、ホテル名、#PRタグが全ての箇所で統一されているか確認する
