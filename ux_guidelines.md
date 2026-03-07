# UX/UI デザインガイドライン

## 🎨 デザイン原則

### 1. カラーパレット・デザインシステム
- **CSS変数の導入**
  - プライマリカラー: ブランドカラー（アメックス: #006fcf）
  - テキストカラー: #1d1d1f（プライマリ）、#86868b（セカンダリ）
  - 背景カラー: #ffffff（プライマリ）、#f5f5f7（セカンダリ）、#fbfbfd（ターシャリ）
  - ボーダーカラー: #d2d2d7
  - 影: 段階的な影（sm/md/lg）
  - 角丸: 12px（標準）、18px（大）

### 2. タイポグラフィ
- **フォントファミリー**
  - Appleライクなフォント: `-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Hiragino Kaku Gothic ProN', 'Hiragino Sans', Meiryo, sans-serif`
  - フォントスムージング: `-webkit-font-smoothing: antialiased`
- **見出しスタイル**
  - h2: 40px, font-weight: 600, letter-spacing: -0.003em
  - h3: 28px, font-weight: 600, letter-spacing: -0.002em
  - h4: 21px, font-weight: 600
- **行間**: 1.7（body）、1.8（段落）

### 3. ヘッダー・ナビゲーション
- **Sticky Header**
  - `position: sticky` で固定
  - スクロール時も常に表示
  - 背景グラデーション適用
  - `backdrop-filter: blur(20px)` でガラス効果
- **目次（Table of Contents）**
  - 固定化せず、スクロールに流れるデザイン
  - スムーズスクロール機能
  - フォントサイズ: 17px（リンク）
  - パディング: 10px 20px
  - ホバーエフェクト: 背景色変化 + 軽い移動

### 4. カード・コンテナデザイン
- **カードコンポーネント**
  - 角丸: `border-radius: 18px`
  - 影: `box-shadow: var(--shadow-sm)`
  - ボーダー: `1px solid var(--border-color)`
  - ホバーエフェクト: `transform: translateY(-2px)` + 影の強化
  - トランジション: `transition: all 0.3s ease`

### 5. テーブルデザイン
- **テーブルスタイル**
  - ヘッダー: グラデーション背景（プライマリカラー）
  - 角丸: `border-radius: 12px`
  - 影: `box-shadow: var(--shadow-sm)`
  - ホバーエフェクト: 行の背景色変化
  - アクセシビリティ: `<caption>` と `scope="col"` を追加

### 6. レスポンシブデザイン
- **モバイル対応**
  - ブレークポイント: `@media (max-width: 768px)`
  - フォントサイズの調整（h2: 32px, h3: 24px, h4: 19px）
  - パディング・マージンの調整
  - テーブルのスクロール対応
  - `scroll-margin-top`: 80px（モバイル）、100px（デスクトップ）

### 7. アクセシビリティ
- **セマンティックHTML**
  - `<header role="banner">`
  - `<main role="main">`
  - `<nav aria-label="目次">`
- **スキップリンク**
  - キーボードナビゲーション対応
  - メインコンテンツへスキップリンク追加
- **ARIA属性**
  - 各ナビゲーションリンクに `aria-label` を追加
  - テーブルに `<caption>` と `scope="col"` を追加

### 8. アニメーション・トランジション
- **スムーズスクロール**: `scroll-behavior: smooth`
- **フェードインアニメーション**: `fadeInUp` キーフレーム
- **ホバーエフェクト**: 軽い移動と影の強化
- **トランジション**: `transition: all 0.3s ease`（標準）

### 9. スペーシング
- **セクション間**: 80px（デスクトップ）、60px（モバイル）
- **カード内パディング**: 32px（デスクトップ）、24px（モバイル）
- **コンテナ最大幅**: 980px（JRE POINT）、max-w-5xl（アメックス）

### 10. コンテンツ構造
- **セクション区切り**: 視覚的な区切りを追加
- **ハイライト**: 重要なテキストを強調
- **情報ボックス**: 左ボーダー + 背景色で強調






























