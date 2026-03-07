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

## 参照

- [SkillsMP - Agent Skills Marketplace](https://skillsmp.com/)
- [anthropics/skills](https://github.com/anthropics/skills)
