# @ino_moneycoach Design Brief

Wise・Airbnb・Rampのデザインエッセンスを統合した、ino_moneycoach専用のデザインガイド。
Claude Codeがhtml制作時に自動参照する。

## デザイン哲学

「金融の信頼感 × 旅の温かみ × 情報の明快さ」

- **Wiseから**: クリーンで誠実。余計な装飾なし。グリーン系のフレッシュな信頼感
- **Airbnbから**: 温かみのある丸み。写真映え。近寄りやすさ
- **Rampから**: データを美しく見せる。数字が主役。余白で呼吸させる

## 用途別トーン

| 用途 | トーン | 参考 |
|------|--------|------|
| GitHub Pages公開ページ | 信頼感＋プレミアム。訪問者が「ちゃんとしてる」と感じる | Wise |
| カルーセル（IG投稿） | 温かみ＋インパクト。スクロール止める太字＋余白 | Airbnb |
| 管理系HTML（自分用） | 視認性最優先。色分け明確。太字。情報密度高め | 現状維持でOK |
| note記事LP | 読みやすさ＋購買意欲。CTA明確 | Wise + Airbnb |

## カラーパレット

### プライマリ
| 名前 | Hex | 用途 |
|------|-----|------|
| **ブランドグリーン** | `#163300` | 見出し・リンク・主要テキスト |
| **アクセントグリーン** | `#9FE870` | CTA・バッジ・ハイライト |
| **ウォームブラック** | `#222222` | 本文テキスト（純黒は使わない） |

### テキスト
| 名前 | Hex | 用途 |
|------|-----|------|
| **Primary** | `#0E0F0C` | 最重要テキスト・見出し |
| **Secondary** | `#454745` | 本文・説明文 |
| **Tertiary** | `#6A6C6A` | プレースホルダー・補足 |

### アクセント（チャネル色分け用）
| 名前 | Hex | 用途 |
|------|-----|------|
| **Rausch Red** | `#FF385C` | CTA・重要期限・アラート |
| **Teal** | `#14C1BD` | REELS・メインアクション（既存ブランドカラー維持） |
| **Orange** | `#F57C00` | STORY・警告 |
| **Purple** | `#533AFD` | NL・プレミアム要素 |
| **Pink** | `#EC407A` | note・収益系 |

### サーフェス
| 名前 | Hex | 用途 |
|------|-----|------|
| **Background** | `#FFFFFF` | ページ背景 |
| **Background Alt** | `#F7F7F7` | セクション交互背景 |
| **Border** | `rgba(14,15,12,0.12)` | カード・仕切り線 |

## タイポグラフィ

### フォントファミリー
```css
--font-display: 'Inter', 'Noto Sans JP', -apple-system, system-ui, sans-serif;
--font-body: 'Noto Sans JP', 'Inter', -apple-system, system-ui, sans-serif;
--font-mono: 'JetBrains Mono', monospace;
```

**方針**:
- 見出し: Inter SemiBold（洗練×読みやすさ）
- 日本語本文: Noto Sans JP Medium（安定した可読性）
- 数字・データ: Inter（プロポーショナル数字が美しい）
- コード: JetBrains Mono

### タイプスケール

| 役割 | サイズ | ウェイト | 行間 | 字間 |
|------|--------|---------|------|------|
| Display | 40px | 700 (Bold) | 1.1 | -1.5% |
| H1 | 30px | 600 (SemiBold) | 1.13 | -1% |
| H2 | 26px | 600 | 1.23 | -0.5% |
| H3 | 22px | 600 | 1.27 | -0.5% |
| H4 | 18px | 600 | 1.33 | -0.5% |
| Body Large | 16px | 500 (Medium) | 1.5 | normal |
| Body | 14px | 400 (Regular) | 1.6 | normal |
| Caption | 12px | 500 | 1.33 | 0.5% |
| KPI数字 | 32-48px | 700 | 1.0 | -1px |

**ルール**:
- 見出しは必ず600以上（細いウェイトは見出しに使わない）
- 本文は400-500（読みやすさ重視）
- 数字を大きく見せるときはBold + 負のletter-spacing
- 純黒(#000)は使わない。常に#222222か#0E0F0C

## レイアウト

### スペーシング
- ベースユニット: 8px
- スケール: 4, 8, 12, 16, 24, 32, 48, 64px
- セクション間: 48-64px
- カード内パディング: 24-32px

### グリッド
- 最大幅: 1080px
- カラム: 2-4列（レスポンシブ）
- ガター: 16-24px

### 余白の哲学
- **Airbnb式**: セクション間にたっぷり余白。スクロールを急がせない
- **データ部分はタイト**: KPI・表はコンパクトに。余白は外側に

## コンポーネント

### ボタン
```css
/* プライマリCTA */
background: #222222;
color: #FFFFFF;
padding: 12px 24px;
border-radius: 8px;
font-weight: 600;
font-size: 16px;
transition: background 0.2s ease;
/* hover: background → アクセントカラー */

/* セカンダリ */
background: transparent;
color: #222222;
border: 1px solid rgba(14,15,12,0.12);
padding: 12px 24px;
border-radius: 8px;
```

### カード
```css
background: #FFFFFF;
border-radius: 16px;
border: 1px solid rgba(14,15,12,0.12);
padding: 24px;
box-shadow: rgba(0,0,0,0.02) 0px 0px 0px 1px,
            rgba(0,0,0,0.04) 0px 2px 6px,
            rgba(0,0,0,0.08) 0px 4px 12px;
transition: box-shadow 0.25s ease, transform 0.25s ease;
/* hover: transform: translateY(-2px); shadow強化 */
```

### KPIカード
```css
background: #FFFFFF;
border-radius: 16px;
padding: 24px 20px;
text-align: center;
border: 1px solid rgba(14,15,12,0.12);
/* 数字: 32-48px, Bold, アクセントカラー */
/* ラベル: 13px, Medium, #6A6C6A */
```

### バッジ・タグ
```css
display: inline-block;
padding: 4px 10px;
border-radius: 6px;
font-size: 12px;
font-weight: 600;
letter-spacing: 0.04em;
/* 色はカテゴリに応じて変更 */
```

### テーブル
```css
/* ヘッダー */
background: #F7F7F7;
font-weight: 600;
font-size: 13px;
color: #0E0F0C;
padding: 12px 16px;
border-bottom: 2px solid rgba(14,15,12,0.12);

/* セル */
padding: 10px 16px;
border-bottom: 1px solid rgba(14,15,12,0.06);
color: #454745;
font-size: 14px;

/* ホバー */
tr:hover td { background: rgba(159,232,112,0.04) }
```

### アラート・ハイライト
```css
/* ハイライト（情報） */
background: rgba(159,232,112,0.08);
border-left: 3px solid #9FE870;
border-radius: 8px;
padding: 16px 20px;
color: #163300;

/* アラート（警告） */
background: rgba(255,56,92,0.06);
border-left: 3px solid #FF385C;
border-radius: 8px;
padding: 16px 20px;
color: #A8200D;
```

## Border Radius スケール

| 用途 | 値 |
|------|-----|
| バッジ・タグ | 6px |
| ボタン・入力 | 8px |
| カード・コンテナ | 16px |
| 大きなカード・ヒーロー | 20px |
| 円形コントロール | 50% |

## シャドウ

| レベル | CSS | 用途 |
|--------|-----|------|
| なし | none | 背景・テキスト |
| 微小 | `0 1px 3px rgba(0,0,0,0.04)` | 控えめなカード |
| 標準 | `rgba(0,0,0,0.02) 0 0 0 1px, rgba(0,0,0,0.04) 0 2px 6px, rgba(0,0,0,0.08) 0 4px 12px` | 通常カード |
| 強調 | `rgba(0,0,0,0.04) 0 0 0 1px, rgba(0,0,0,0.06) 0 4px 12px, rgba(0,0,0,0.12) 0 8px 24px` | ホバー・フロート |

## アニメーション

- ホバー: `transform: translateY(-2px)` + シャドウ強化（0.25s ease）
- ページ読み込み: `fadeUp`（opacity 0→1, translateY 16px→0）、0.4s ease-out、セクションごとに0.05sずつ遅延
- トランジション: 色変化は0.2s ease、移動は0.25s ease
- **やりすぎない**: 1ページ1アニメーション演出で十分

## やること・やらないこと

### Do
- テキストは `#222222` か `#0E0F0C`（温かみのある黒）
- CTAは1色に絞る（ページ内で最も目立つ色）
- カードは16px以上のborder-radius（柔らかさ）
- 3層シャドウで自然な浮き上がり
- 日本語フォントはNoto Sans JP Medium以上
- データ・数字はInter Bold + 大きめサイズ
- 余白はたっぷり。特にセクション間

### Don't
- 純黒 `#000000` をテキストに使わない
- 5色以上を1画面で同時に使わない
- border-radius 4px以下のシャープな角は使わない（管理系HTMLを除く）
- 影を1層だけで済ませない（最低2層）
- Inter/Noto Sans以外の日本語フォントを安易に使わない
- アニメーションを3箇所以上に入れない
