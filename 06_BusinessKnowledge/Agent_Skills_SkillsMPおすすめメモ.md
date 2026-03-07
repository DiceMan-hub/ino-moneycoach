# SkillsMP から選ぶ「本当に使える」Agent Skills

普段の作業（ニュースレター・note・議事録・プロジェクト管理）で Claude Code と組み合わせて使えそうなスキルを、SkillsMP と Anthropic 公式を元に整理したメモ。

---

## 1. 作業に直結しそうなもの（SkillsMP Business で確認済み）

| スキル | 提供元 | 用途 | 相性 |
|--------|--------|------|------|
| **meeting-notes** | Shubhamsaboo/awesome-llm-apps | 議事録・アクションアイテム・決定事項の構造化 | ◎ `05_Minutes/` の議事録作成・整理 |
| **project-planner** | 同上 | プロジェクトのタスク分解・マイルストーン・依存関係 | ◎ `07_Management/` のグランドプラン・タスク管理 |
| **content-design** | n8n-io/n8n | ボタンラベル・CTA・エラーメッセージ等のUIコピー設計 | △ ニュースレターのCTA・見出しの言い回しの参考 |
| **authoring-skills** | vercel/next.js | SKILL.md の書き方・frontmatter・説明文の設計 | ◎ `.agent/skills` / `.claude/skills` を増やすときの参考 |

- **meeting-notes** / **project-planner** は「議事録」「プロジェクト計画」と言うと Claude Code がロードしやすく、そのまま使える可能性が高い。
- **content-design** は n8n 向けだが、ニュースレターのCTAや見出しの言い回しの参考になる。

---

## 2. Anthropic 公式（anthropics/skills）で有用なもの

| スキル | 用途 | 相性 |
|--------|------|------|
| **doc-coauthoring** | ドキュメント・提案・仕様の共著ワークフロー（文脈収集→構成→読者テスト） | ◎ note 記事・ニュースレター段取り・長文の設計 |
| **internal-comms** | 社内向けアップデート・ニュースレター・FAQ・ステータス報告のフォーマット | △ テンプレを「週刊マイル・ポイント通信」用にカスタムすれば流用可 |
| **skill-creator** | スキルの作り方・メタデータ・例の書き方 | ◎ 既存の .agent/skills を増やしたり品質を上げるのに使える |
| **brand-guidelines** | ブランド色・タイポグラフィの適用 | △ 色やフォントの統一が必要な資料・HTML用（中身は Anthropic 向けなので参考程度） |

- インストール: [SkillsMP の FAQ](https://skillsmp.com/) のとおり、`~/.claude/skills/` またはプロジェクトの `.claude/skills/` に、該当リポジトリから SKILL.md を含むフォルダをコピーすればよい。公式は `anthropics/skills` を marketplace として登録してプラグイン経由でも入れられる。

---

## 3. おすすめの「最初の1本」

- **議事録をよく書く** → **meeting-notes**（awesome-llm-apps 系）
- **note・ニュースレターの構成・長文を一緒に組みたい** → **doc-coauthoring**（anthropics/skills）
- **スキルを自分で増やしたい** → **skill-creator**（anthropics/skills）

SkillsMP は「検索・カテゴリ」で候補を探し、**実際に使うスキルは GitHub の SKILL.md を読んでから導入**するのが安全。上記のいずれかから 1 本入れて試すのがおすすめ。

---

## 4. SkillsMP のレビュー・評価と信頼性の見方

### 現状：ユーザーレビューや評価はない

- **レビュー・評価**: SkillsMP には**ユーザーによるレビューや星評価はない**。運営も「Quality curation is our next priority」と [About](https://skillsmp.com/about) で述べており、**これから**整える段階。
- **予定されている機能**（未実装）:
  - ドメイン別の専門家による検証
  - 品質フィルターで良質なスキルを表示
  - **コミュニティの評価・利用統計**

### 今ある「信頼の手がかり」

| 手がかり | 内容 |
|----------|------|
| **最低スター数** | 2 stars 未満のリポジトリは除外（[FAQ: Are these skills safe?](https://skillsmp.com/)） |
| **基本品質スキャン** | 簡単な品質指標のスキャンは行っている（詳細は非公開） |
| **最終更新日** | 各スキルカードに「最終更新日」が表示される。古いほどメンテされていない可能性 |
| **提供元** | カードに「from "org/repo"」で出る。anthropics/skills・vercel/next.js など有名リポジトリは信頼の一要素 |

### 信頼できるかどうかを自分で確かめる方法

1. **GitHub でリポジトリを開く**  
   スキル詳細のリンクから元 repo へ行き、Stars・Issues・最終コミット日を確認。
2. **SKILL.md を読む**  
   中身が具体的で「いつ使うか」「何をしてはいけないか」が書いてあれば、設計されているスキルと判断しやすい。
3. **スクリプトや依存があるなら中身を確認**  
   `scripts/` や外部コマンドを呼ぶ場合は、オープンソースと同様に**導入前にコードを確認**する。
4. **公式・有名プロダクト由来を優先**  
   anthropics/skills・n8n-io/n8n・vercel/next.js など、公式またはよく知られたプロジェクトのスキルは、運用方針が読みやすい。

**まとめ**: 現時点では「SkillsMP の評価」ではなく、**GitHub のスター・更新頻度・SKILL.md の内容・提供元**で信頼性を判断する必要がある。FAQ の「inspect before use」のとおり、**導入前に必ず中身を確認する**のが安全。

---

## 5. Claude Code で順次テストする手順

### 5.1 インストール場所を決める

| 場所 | 向き |
|------|------|
| **プロジェクト** `.claude/skills/`（この vault 内） | このリポジトリでだけ使うスキル。Git で管理できる。 |
| **グローバル** `~/.claude/skills/` | どのプロジェクトでも使うスキル。 |

→ まずは**プロジェクト**に置いて試すと、影響範囲が分かりやすく、不要ならフォルダを消すだけでロールバックできる。

### 5.2 1本ずつ入れて試す流れ

1. **1スキルだけ入れる**  
   複数まとめて入れない。どのスキルの効果か切り分けやすくする。
2. **GitHub から取得**  
   - スキルが単体 repo なら clone、サブフォルダならそのフォルダだけコピー。  
   - 必ず **SKILL.md が入ったフォルダ**を `.claude/skills/<スキル名>/` として配置する。
3. **Claude Code を再起動 or 新セッション**  
   スキルは起動時に読み込まれるため、追加後は新しいチャットを開くか IDE を開き直す。
4. **スキルを「発火」させる**  
   スキルは**モデルが文脈で判断してロード**する。依頼文に**そのスキルのトリガーになる語**を入れる。
   - 例: meeting-notes → 「この会話から議事録を作って」「アクションアイテムを整理して」
   - 例: project-planner → 「このプロジェクトをタスク分解して」「マイルストーンを立てて」
   - 例: doc-coauthoring → 「この note の構成を一緒に組みたい」「提案書を共著で書きたい」
5. **結果をひと目で分かる形でメモ**  
   使えた / 微妙 / 要カスタム / やめた、のいずれかと、一言理由を残す（下記テストログ参照）。

### 5.3 トリガー例（依頼時に含めるとスキルが選ばれやすい）

| スキル | 依頼の例 |
|--------|----------|
| meeting-notes | 「議事録にして」「アクションアイテムを抽出して」「決定事項をまとめて」 |
| project-planner | 「タスク分解して」「マイルストーンを立てて」「依存関係を整理して」 |
| doc-coauthoring | 「共著でドキュメントを書きたい」「提案書の構成から一緒にやりたい」 |
| skill-creator | 「新しいスキルを作りたい」「SKILL.md の書き方を教えて」 |
| internal-comms | 「社内ニュースレターのテンプレが欲しい」「ステータス報告のフォーマット」 |

### 5.4 テストログ（コピーして使う）

テストした日と結果だけ残す用。このメモの下に追記しても、別ファイル（例: `Agent_Skills_テストログ.md`）にしてもよい。

```markdown
| スキル名 | 導入日 | 結果 | メモ |
|----------|--------|------|------|
| meeting-notes | YYYY-MM-DD | 未 / 採用 / 要カスタム / 見送り |  |
| project-planner |  |  |  |
| doc-coauthoring |  |  |  |
| skill-creator |  |  |  |
| internal-comms |  |  |  |
```

### 5.5 やめる場合

- そのスキルのフォルダを `.claude/skills/` から削除するだけ。  
- 次の Claude Code セッションからは読み込まれない。

---

## 参照

- [SkillsMP - Agent Skills Marketplace](https://skillsmp.com/)
- [anthropics/skills](https://github.com/anthropics/skills)
