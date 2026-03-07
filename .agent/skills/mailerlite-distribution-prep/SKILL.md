---
name: MailerLite Distribution Prep
description: ニュースレターのMailerLite配信準備を行うスキル。Vol.07の実績に基づき、変数設定、リンク検証、最終チェックを実施します。
---

# MailerLite Distribution Prep Skill

## 🎯 概要

このスキルは、ニュースレター作成の**Phase 6: 配信準備**をサポートします。

**使用タイミング:**

- HTML変換と整合性チェックが完了した後
- 配信直前の最終確認時
- note記事URLを設定する時

**所要時間目安:** 約 10 分

**前提スキル:** `newsletter-consistency-check` で整合性チェックが完了していること

---

## 📋 配信準備フレームワーク（Vol.07実績ベース）

### Step 1: MailerLite変数の確認（3 分）

#### 必須変数

| 変数 | 用途 | 配置場所 |
|------|------|----------|
| `{$url}` | ブラウザ表示用リンク | ヘッダー部分 |
| `{$unsubscribe}` | 配信停止リンク | フッター部分 |

#### 確認方法

```bash
# 変数の存在確認
grep "{\$url}" newsletter.html
grep "{\$unsubscribe}" newsletter.html
```

#### 正しい配置例（Vol.07実績）

**ブラウザ表示リンク:**
```html
メールが正しく表示されない場合は<a href="{$url}" style="color: #14c1bd; text-decoration: underline">こちらからブラウザで表示</a>
```

**配信停止リンク:**
```html
<a href="{$unsubscribe}" style="color: #999999; text-decoration: underline">配信停止はこちら</a>
```

---

### Step 2: note記事URLの設定（3 分）

**Vol.07の実績:** `https://bit.ly/3YFF0m5`

#### プレースホルダーの確認

```bash
# プレースホルダーの検索（あってはいけない）
grep "note記事URL" newsletter.html
```

#### 置き換え

**Before:**
```html
href="note記事URL"
```

**After:**
```html
href="https://bit.ly/XXXXXXX"
```

#### 確認箇所（Vol.07で2箇所）

- [ ] 冒頭のCTAボタン
- [ ] 後半のCTAボタン

**重要:** 両方のCTAボタンのURLを置き換えること

---

### Step 3: 全リンクの検証（3 分）

#### チェック項目

- [ ] 全ての外部リンクが有効
- [ ] 短縮URL（bit.ly）が正しくリダイレクト
- [ ] アフィリエイトリンクが正しく設定
- [ ] **リンク色が `#14c1bd` で統一されている**

#### 検証方法

```bash
# 全リンクの抽出
grep -oP 'href="[^"]*"' newsletter.html | sort | uniq

# 赤色リンクの確認（あってはいけない）
grep -i "color.*#e53935\|color.*red" newsletter.html
```

#### 主要リンクの確認

| リンク種別 | 確認項目 |
|-----------|----------|
| note記事 | URLが正しい、記事が公開されている |
| 公式サイト | リンク先が正しい |
| アフィリエイト | パラメータが正しい、#PRタグが付いている |
| Instagram | プロフィールリンクが正しい |

---

### Step 4: HTML構造の最終確認（2 分）

#### チェック項目

- [ ] DOCTYPE宣言がある
- [ ] `<html lang="ja">` が設定されている
- [ ] `<meta charset="utf-8">` がある
- [ ] `<title>` が正しく設定されている
- [ ] テーブルベースのレイアウト
- [ ] インラインスタイルのみ使用

#### 確認方法

```bash
# HTMLヘッダーの確認
head -30 newsletter.html
```

---

### Step 5: プレビュー確認（5 分）

#### 確認方法

1. **ブラウザプレビュー**
   ```bash
   open -a Safari newsletter.html
   ```

2. **MailerLiteプレビュー**
   - MailerLiteにHTMLをアップロード
   - プレビュー機能で確認
   - テストメール送信

#### チェック項目

- [ ] レイアウトが正しく表示される
- [ ] 画像が正しく表示される（該当する場合）
- [ ] リンクがクリック可能
- [ ] CTAボタンが目立つ
- [ ] モバイル表示が正しい

---

## 📋 配信前最終チェックリスト（Vol.07実績ベース）

### MailerLite変数

- [ ] `{$url}` がヘッダーに設定されている
- [ ] `{$unsubscribe}` がフッターに設定されている

### note記事URL

- [ ] プレースホルダー（`note記事URL`）が全て置き換えられている
- [ ] note記事が公開されている
- [ ] URLが正しくリダイレクトする
- [ ] **2箇所のCTAボタン両方が更新されている**

### リンク

- [ ] 全ての外部リンクが有効
- [ ] アフィリエイトリンクが正しい
- [ ] **リンク色が `#14c1bd` で統一されている**

### HTML構造

- [ ] DOCTYPE宣言がある
- [ ] メタタグが正しい
- [ ] テーブルベースのレイアウト

### プレビュー

- [ ] ブラウザで正しく表示される
- [ ] MailerLiteプレビューで確認済み

---

## 🚨 よくある問題と対処法（Vol.07実績ベース）

### 問題1: プレースホルダーが残っている

**症状:** `note記事URL` がそのまま表示される

**対処:**
```bash
# 検索
grep "note記事URL" newsletter.html

# 置換（2箇所あることに注意）
sed -i '' 's/note記事URL/https:\/\/bit.ly\/XXXXXXX/g' newsletter.html
```

### 問題2: CTAボタンのURLが1箇所しか更新されていない

**症状:** 冒頭のCTAは更新されているが、後半のCTAが古いまま

**対処:**
- 両方のCTAボタンを確認
- `grep` で `href` を検索して全箇所を確認

### 問題3: リンク色が統一されていない

**症状:** 一部のリンクが赤色（`#e53935`）になっている

**対処:**
```bash
# 赤色リンクの検索
grep -i "color.*#e53935\|color.*red" newsletter.html

# 置換
sed -i '' 's/#e53935/#14c1bd/g' newsletter.html
```

### 問題4: MailerLite変数が認識されない

**症状:** `{$url}` がそのまま表示される

**対処:**
- MailerLiteの変数構文を確認
- HTMLエスケープされていないか確認

### 問題5: レイアウトが崩れる

**症状:** テーブルが正しく表示されない

**対処:**
- `width="600"` が設定されているか確認
- インラインスタイルが正しいか確認
- `border-collapse: collapse` が設定されているか確認

---

## ✅ 完了チェックリスト

配信準備完了時に以下を確認：

- [ ] MailerLite変数が正しく設定されている
- [ ] note記事URLが実際のURLに置き換えられている（2箇所）
- [ ] 全てのリンクが有効
- [ ] リンク色が `#14c1bd` で統一されている
- [ ] HTML構造が正しい
- [ ] プレビューで確認済み

---

## 📊 配信後のアクション（Vol.07実績ベース）

1. **アーカイブフォルダに保存**
   ```
   03_NewsLetter/_archive/2026/Vol0X_第X号/
   ```

2. **保存するファイル**
   - `2026_MM_DD_Vol0X_いのマネーニュースレター.html`
   - `2026_MM_DD_Vol0X_いのマネーニュースレター_ドラフト.md`
   - `README.md`（概要）
   - `作業記録_Vol0X.md`（作業内容の詳細）

3. **次号の準備** → `newsletter-planning` スキルに戻る

---

## 📚 参考資料

**実際に存在するファイル:**
- `03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター.html` - Vol.07の実績HTMLファイル
- `03_NewsLetter/_archive/2026/Vol07_第7号/作業記録_Vol07.md` - Vol.07の作業記録
- `03_NewsLetter/_archive/2026/Vol07_第7号/README.md` - Vol.07の概要

---

## 💡 Vol.07で学んだ教訓

1. **2箇所のCTAボタン**: 冒頭と後半の両方のURLを更新すること
2. **bit.ly短縮URL**: note記事公開後にbit.lyでURLを短縮し、設定する
3. **リンク色の最終確認**: 配信前に赤色リンクがないか最終確認する
4. **アーカイブの重要性**: 配信後は必ずアーカイブフォルダに保存し、作業記録を残す
5. **HTMLとMarkdownの両方を保存**: 次号の参考のため、両方のファイルを保存する
