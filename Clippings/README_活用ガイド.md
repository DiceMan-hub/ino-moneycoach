# Clippings 活用ガイド

Web記事クリップ（`processed/`）を、ニュースレター・note・リサーチから**確実に再利用する**ためのルールとワークフロー。

---

## 1. 活用の原則

- **Clippings は「外部記事のナレッジベース」**：Web記事をカテゴリ + key_facts で整理済み。他プロジェクトは**参照元としてリンク**し、重複執筆を避ける。
- **参照は Obsidian の `[[リンク]]` で行う**：プロジェクト側のドキュメントから「どのClipping記事を参照したか」を明示する。
- **`use_for` フィールドで絞る**：目的に合った記事を素早くピックできる。

---

## 2. プロジェクト別の活用パターン

### ニュースレター（03_NewsLetter）

| フェーズ | 使い方 |
|:--|:--|
| **企画** | `Clippings/_index.md` を流し読み → `use_for: newsletter` の記事をピック |
| **特集執筆** | 選んだClipping記事の `key_facts` を参照元として開き、要約・体験・追記をドラフトに書く |
| **速報ネタ** | `status: active` かつ直近の記事を「今週のトピック」に |

**段取りへの組み込み例：**

```markdown
### 今号で参照する Clippings（2〜3本に絞る）
- [[Clippings/processed/ホテル/【日系ホテルチェーン初】 東急ホテルズ、Global Hotel Alliance（GHA）へ加盟]]
- [[Clippings/processed/マネー・節税/ふるなびマネー提供開始]]
```

---

### note・記事（04_note / ブログ）

| 用途 | 使い方 |
|:--|:--|
| **記事の種** | `use_for: note` の記事を種にして、自分の体験・分析を加えて1本の記事に拡張 |
| **根拠・出典** | 記事内で「こういう情報がある」と書くとき、`[[Clippings/processed/カテゴリ/タイトル]]` をリンク |
| **シリーズ化** | 例：AI・テック配下の確定申告系2記事 → 「AIで確定申告を攻略」特集 |

---

### リサーチ（06_Research）

| 用途 | 使い方 |
|:--|:--|
| **インプット** | `use_for: research` の記事を起点に深掘り調査 |
| **比較・一覧** | 既存リサーチに Clipping 記事の `key_facts` をエビデンスとして追加 |
| **トレンド把握** | カテゴリ別に時系列で並べ、動向を読む |

---

## 3. frontmatter フィールド一覧

| フィールド | 用途 | 値の例 |
|:--|:--|:--|
| `category` | カテゴリ名（processed/のサブフォルダ名と一致） | マイレージ, ホテル, AI・テック, マネー・節税, 海外金融・資産 |
| `status` | 記事の有効性 | active / expired / archived |
| `use_for` | 活用先 | newsletter, note, research, reference |
| `key_facts` | 記事要点3行以内 | リスト形式 |
| `processed` | 構造化処理した日付 | 2026-03-07 |
| `expiry` | キャンペーン期限（該当時のみ） | 2025-12-31 |
| `related` | 関連ノートへのリンク（任意） | `[[LINE/processed/...]]` |

---

## 4. 運用フロー

```
クリップ → inbox/ に保存
     ↓
処理（手動 or 将来Skill化）
  category判定 → key_facts抽出 → use_for設定 → tags拡張
     ↓
processed/カテゴリ/ に移動 + _index.md 更新
     ↓
NL企画 / note / リサーチ から [[Clippings/processed/...]] で参照
     ↓
活用後: status → archived
```

---

## 5. 運用ルール（推奨）

1. **参照したらリンクを残す**
   ニュースレターの段取り・ドラフト、noteの下書きに `[[Clippings/processed/カテゴリ/タイトル]]` を1行書く。

2. **インデックスは MOC のまま使う**
   `Clippings/_index.md` はカテゴリ別・日付順。企画時はここから選ぶ。

3. **期限切れ記事に注意**
   `status: expired` / `expiry` が過去の記事は、参照時に「当時のキャンペーン。現在は要確認」と一文添える。_index.md では ⚠️ マーカー付き。

4. **1号・1記事あたり 2〜3 本まで**
   多く参照しすぎると焦点がぼける。

---

## 6. クイック参照

| やりたいこと | 開くもの |
|:--|:--|
| NLのネタを探す | [[Clippings/_index]] → `use_for: newsletter` の記事 |
| noteの種を見つける | [[Clippings/_index]] → `use_for: note` の記事 |
| リサーチの起点 | [[Clippings/_index]] → `use_for: research` の記事 |
| 新着クリップを処理 | [[Clippings/inbox/]] → frontmatter追加 → processed/ へ移動 |
