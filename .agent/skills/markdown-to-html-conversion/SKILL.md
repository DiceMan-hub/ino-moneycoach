---
name: Markdown to HTML Conversion
description: ニュースレターのMarkdownドラフトをMailerLite配信用HTMLに変換するスキル。Vol.07の実績フォーマットを踏襲し、一貫性のあるHTMLを生成します。
---

# Markdown to HTML Conversion Skill

## 🎯 概要

このスキルは、ニュースレター作成の**Phase 3-4: HTML変換**をサポートします。

**使用タイミング:**

- Markdownドラフトが完成した後
- HTMLファイルを作成する時
- Vol.07のフォーマットを適用する時

**所要時間目安:** 約 30-60 分（手動）→ 自動化により 5-10 分に短縮可能

**前提スキル:** `content-research` で情報収集が完了していること、Markdownドラフトが完成していること

---

## 📋 変換フレームワーク

### Step 1: テンプレートの選択（5 分）

#### ベーステンプレートの確認

**実際に存在するファイル:**
```
03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター.html  ← 最新の実績ファイル（推奨）
03_NewsLetter/_template/テンプレート_いのマネーニュースレター.html  ← 汎用テンプレート
```

**重要:** Vol.07のHTMLファイルを主な参考にする。これが最新の実績フォーマット。

#### HTML構造の確認

- テーブルベースのレイアウト（`<table role="presentation">`）
- インラインスタイル使用（外部CSSなし）
- MailerLite変数（`{$url}`, `{$unsubscribe}`）の配置
- レスポンシブ対応（メディアクエリ）

---

### Step 2: 基本構造の変換（15 分）

#### HTMLヘッダー

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8" />
  <title>いのマネーニュースレター Vol.XX｜[タイトル]</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <style>
    @media only screen and (max-width: 600px) {
      .wrapper { width: 100% !important; }
      .content { padding: 16px !important; }
      h1 { font-size: 22px !important; line-height: 1.4 !important; }
      h2 { font-size: 18px !important; }
      .toc-box { padding: 16px !important; }
      .highlight-box { padding: 16px !important; }
    }
  </style>
</head>
```

#### メタ情報の変換

- **配信日**: Markdownの「配信日時」から抽出
- **件名**: Markdownの「件名案」から抽出
- **タイトル**: h1タグに変換

---

### Step 3: コンテンツの変換（20 分）

#### セクション変換ルール

| Markdown | HTML |
|----------|------|
| `## セクション` | `<h2 style="...">セクション</h2>` |
| `### サブセクション` | `<h3 style="...">サブセクション</h3>` |
| `**太字**` | `<strong>太字</strong>` |
| `[リンク](URL)` | `<a href="URL" style="color: #14c1bd;">リンク</a>` |
| `- リスト` | `<ul><li>リスト</li></ul>` |

#### テーブルの変換（Vol.07実績スタイル）

**Markdown形式:**
```markdown
| サービス | 期限・開始 |
|---|---|
| [タイトル](URL) 説明 | 日付 |
```

**HTML形式（Vol.07スタイル）:**
```html
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse; margin: 16px 0;">
  <tr style="background-color: #f8f9fa">
    <th style="width: 35%; padding: 10px 12px; text-align: left; font-size: 13px; font-weight: 600; border: 1px solid #e0e0e0;">サービス</th>
    <th style="padding: 10px 12px; text-align: left; font-size: 13px; font-weight: 600; border: 1px solid #e0e0e0;">概要</th>
  </tr>
  <tr>
    <td style="padding: 10px 12px; border: 1px solid #e0e0e0; vertical-align: top;">
      <a href="URL" style="color: #14c1bd; text-decoration: underline;">タイトル</a>
      <div style="font-size: 11px; color: #888; margin-top: 4px;">日付</div>
    </td>
    <td style="padding: 10px 12px; border: 1px solid #e0e0e0; font-size: 13px; line-height: 1.6;">説明</td>
  </tr>
</table>
```

**重要なポイント:**
- 第1列: 35%幅（サービス名 + 日付）
- 第2列: 65%幅（概要）
- 日付は小さめのフォント（11px）でタイトル下に配置
- **全てのリンクは `#14c1bd` で統一**（赤色は使用しない）

---

### Step 4: CTAボタンの変換（10 分）

#### 冒頭の小さめCTAボタン（Vol.07で追加）

**配置**: ハイライトリストの直後

**スタイル（Vol.07実績）:**
```html
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="margin: 0 0 16px 0">
  <tr>
    <td align="center">
      <table role="presentation" cellpadding="0" cellspacing="0" style="margin: 0 auto">
        <tr>
          <td align="center" style="background-color: #14c1bd; border-radius: 4px; padding: 10px 20px;">
            <a href="URL" style="display: inline-block; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 12px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; cursor: pointer; line-height: 1.4;">
              タイトル →
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

#### 後半の大きなCTAボタン

**配置**: メインコンテンツセクションの最後

**スタイル（Vol.07実績）:**
```html
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="margin: 24px 0;">
  <tr>
    <td align="center">
      <table role="presentation" cellpadding="0" cellspacing="0" style="margin: 0 auto">
        <tr>
          <td align="center" style="background-color: #14c1bd; border-radius: 6px; padding: 14px 32px;">
            <a href="URL" style="display: inline-block; color: #ffffff; text-decoration: none; font-weight: 600; font-size: 15px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; cursor: pointer;">
              【年会費の1.6倍の価値?!】タイトル →
            </a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>
```

**CTAボタンの必須要素（Vol.07で確立）:**
- 矢印（→）を末尾に追加
- 中央揃え（`align="center"` + `margin: 0 auto`）
- `cursor: pointer;` を追加
- タイトルを含める（長い場合は `font-size: 12px` + `line-height: 1.4`）

---

### Step 5: 特殊要素の変換（10 分）

#### 引用ブロック（>）

```html
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background-color: #fff8e1; border-radius: 6px; border-left: 4px solid #ffc107; margin: 16px 0;">
  <tr>
    <td style="padding: 16px 20px;">
      <div style="font-size: 14px; font-weight: 600; color: #f57c00; margin-bottom: 8px;">
        📖 タイトル:
      </div>
      <div style="font-size: 13px; line-height: 1.8; color: #444444;">
        内容
      </div>
    </td>
  </tr>
</table>
```

#### 目次ボックス

```html
<table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f9fafa; border-radius: 6px; border-left: 4px solid #14c1bd; margin: 16px 0;">
  <tr>
    <td style="padding: 20px 24px;">
      <div style="font-size: 13px; font-weight: 600; color: #14c1bd; margin-bottom: 12px;">
        📋 今号の目次
      </div>
      <div style="font-size: 14px; line-height: 1.6;">
        1. 📰 今週の注目ニュース<br>
        2. 🎯 メインコンテンツ<br>
        ...
      </div>
    </td>
  </tr>
</table>
```

---

## 🎨 スタイルガイドライン（Vol.07実績）

### カラーパレット

- **プライマリカラー**: `#14c1bd` (リンク、CTAボタン) ← **全てのリンクはこの色で統一**
- **テキスト**: `#333333` (本文), `#222222` (見出し)
- **背景**: `#ffffff` (メイン), `#f5f5f5` (外側)
- **アクセント**: `#ffc107` (警告ボックス), `#f57c00` (警告テキスト)
- **日付・補足**: `#888888` (小さめテキスト)

**注意:** 赤色（`#e53935`等）はリンクに使用しない（Vol.07で修正した経緯あり）

### フォント

```html
font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

### リンクスタイル

```html
style="color: #14c1bd; text-decoration: underline;"
```

---

## ✅ 完了チェックリスト（Vol.07実績ベース）

HTML変換完了時に以下を確認：

- [ ] HTMLヘッダーが正しく設定されている
- [ ] メタ情報（タイトル、配信日）が正しい
- [ ] テーブル構造がVol.07スタイル（35%/65%）になっている
- [ ] **CTAボタンが2箇所に配置されている（冒頭・後半）**
- [ ] **全てのリンクが `#14c1bd` で統一されている（赤色なし）**
- [ ] CTAボタンに矢印（→）が追加されている
- [ ] CTAボタンが中央揃えになっている
- [ ] MailerLite変数（`{$url}`, `{$unsubscribe}`）が設定されている
- [ ] レスポンシブスタイルが含まれている
- [ ] インラインスタイルのみ使用（外部CSSなし）

---

## 📚 参考資料

**実際に存在するファイル:**
- `03_NewsLetter/2026_01_17_Vol07_いのマネーニュースレター.html` - Vol.07の実績HTMLファイル（最新の参考）
- `03_NewsLetter/_template/テンプレート_いのマネーニュースレター.html` - 汎用テンプレート
- `03_NewsLetter/_archive/2026/Vol07_第7号/作業記録_Vol07.md` - Vol.07の作業記録

---

## 🔗 次のスキル

HTML変換完了後は、以下のスキルに進む：

1. **newsletter-consistency-check** - HTMLとMarkdownの整合性チェック
2. **newsletter-format-standardization** - 表記の統一確認
3. **mailerlite-distribution-prep** - 配信準備

---

## 💡 Vol.07で学んだ教訓

1. **リンク色の統一**: SBIハイパー預金のリンクが赤色だったため、`#14c1bd`に統一した
2. **CTAボタンの配置**: 冒頭にも小さめのCTAボタンを追加することで、導線を強化
3. **矢印の追加**: CTAボタンにリンクであることが分かるよう「→」を追加
4. **中央揃え**: CTAボタンは中央揃えが視認性が高い
5. **タイトルの長さ対応**: 長いタイトルは `font-size: 12px` + `line-height: 1.4` で対応
