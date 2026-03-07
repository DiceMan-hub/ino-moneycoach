# **AI時代の知的生産と開発戦略：バイブコーディングとMarkdownナレッジ基盤の統合レポート**

> **読者へのメモ：** このレポートは、AIやプログラミングにこれから触れる方でも理解できるよう、専門用語にはできるだけ補足を入れています。初めて見る用語は、文中で「（＝〇〇）」のように説明を添えています。

## **1. はじめに・本レポートの目的**

いま、仕事や勉強のやり方を変える「二つの柱」があります。

**一つ目は「バイブコーディング」です。**  
プログラミングの書き方を詳しく知らなくても、AIに「こんな画面を作って」「この機能を追加して」と日本語や英語で頼むだけで、Webサイトやアプリのたたき（プロトタイプ）から、そのまま使えるコードまでを作ってもらえる開発のやり方です。2026年ごろから、こうした「AIに作らせる開発」が当たり前になりつつあります。

**二つ目は「Markdown（マークダウン）」です。**  
Markdownは、メモやドキュメントを書くときの共通の書き方（＝軽量マークアップ）です。どの編集ソフト（＝IDEやツール）を使っても扱いやすく、AIが読みやすい形式として、いまの事実上の標準になっています。

このレポートでは、この二つをセットで扱います。「メモや仕様をMarkdownで書く・蓄える」と「AIにバイブコーディングで開発させる」を、個人でも組織でも一貫して使えるようにするための指針をまとめました。ナレッジ管理（ObsidianとGoogle Workspaceの比較、**RAG**＝第2章で説明・AIがあなたのメモを検索して参照し、その内容を踏まえて答える仕組みとの相性）と、バイブコーディングに使うツール・進め方・12ヶ月のロードマップを一つの流れで説明します。

---

## **2. 基盤としてのMarkdown：なぜ「書式」の選択が大切か**

Markdownは2004年頃に生まれた、**人間にも機械にも読みやすい文書の書き方**です。難しいHTMLタグを使わず、`#` で見出し、`-` で箇条書きのように、シンプルな記号で構造を表します。いま、ドキュメントの世界では「共通語」のように使われており、開発ツールやAIとも相性が良いことが理由の一つです。

### **2.1 Docs-as-Code（ドキュメントも「コード」のように扱う）**

**Docs-as-Code**とは、「説明書や仕様書も、プログラムのソースコードと同じやり方で管理しよう」という考え方です。

- ドキュメントを**プレーンテキスト**（＝普通のテキストファイル）で書くので、**Git**（＝変更履歴を残すツール）で「誰がいつ何を直したか」を追え、複数人で編集しても競合（コンフリクト）を整理しやすいです。
- コード用の仕組み（課題管理、レビュー、自動テスト）をそのままドキュメントにも使えます。
- 例：Markdownを保存するたびに自動でWebサイトを更新したり、リンク切れをチェックしたりできます。Google Docsのようなクラウドのワープロだけでは、ここまで自動化するのは難しいです。

### **2.2 データを「自分のもの」として持つ（データ主権）**

特定の会社のサービスや独自形式にだけデータを置いていると、サービスが終了したり別のツールに移りたくなったときに、**データを取り出しにくい・形が崩れる**というリスクがあります。

Markdownは**ただのテキストファイル**なので、どのアプリにも縛られません。これを**データ主権**（＝自分のデータを自分でコントロールできる状態）が保てる、と表現します。テキストエディタがあれば、何年後でも、どのOS・どのデバイスでも開けます。長く知識を蓄えるには、この「持ち運びやすさ」がとても重要です。

### **2.3 AI（LLM・RAG）とMarkdownの相性が良い理由**

**LLM（大規模言語モデル）**は、ChatGPTやClaude、Geminiなどの「文章を理解して生成するAI」の基盤技術です。**RAG（検索拡張生成）**は、**AIがあなたのメモやドキュメントを検索して参照し、その内容を踏まえて答える**仕組みです。元のデータがMarkdownかどうかで、AIの**答えの質・速さ・コスト**が大きく変わります。

- **AIが理解しやすい形である：** HTMLやWordは装飾用のタグが多く、AIが「本当に大事な中身」を取り出すのに無駄な処理（＝トークン消費）が増え、ノイズも入りやすいです。Markdownは見出しが `#` 一つで表せるなどシンプルで、多くのAIはGitHubなどのMarkdownを大量に学習しているため、「母国語に近い」形として高精度に解釈します。
- **RAGの「チャンキング」に有利：** 長い文書をAIに渡すとき、適切な**かたまり（チャンク）**に分ける必要があります。Markdownなら見出し（`#`、`##`）が「区切りの目印」になるので、**トピックごとにきれいに分割**しやすく、AIに渡す文脈が正確になります。また、ファイルの先頭に書く**YAMLフロントマター**（日付・タグ・公開範囲など）をメタデータとして使えば、「〇〇タグが付いた最近のメモだけ参照して」のように条件を付けられ、AIの**ハルシネーション**（＝事実と違うことを自信満々に言う現象）を減らしやすくなります。
- **「全部まとめて渡す」より「Markdownで整理してからRAG」の方が得：** Obsidianのように、自分のノート一式をRAG用にインデックスして、ローカルでAIと対話するやり方なら、プライバシーを守りつつ「自分の知識」で答えさせられます。反対に、Gemini 1.5のように「何百ページもまとめて一度に渡す」やり方は、**本当に必要な情報をAIが見落としやすくなる**・API料金や応答時間が増える、といったトレードオフがあります。**Markdownで構造化し、適切にチャンキングしたRAG**の方が、コスト・速度・精度のバランスで有利になることが多いです。

---

## **3. ナレッジ管理の選択肢：ObsidianとGoogle Workspace**

Markdownのメモやドキュメントを「どこに置いて、どう編集するか」には、主に二つのスタイルがあります。**パソコン内のフォルダを中心にするObsidian**と、**クラウド（インターネット上）でみんなで共有するGoogle Workspace**です。

### **3.1 Obsidian：ノート同士を「リンク」でつなぐ使い方**

**Obsidian**は、あなたのパソコンにある**Markdownのフォルダ（Vault＝「保管庫」）**を開いて、ノート同士のつながりを可視化・検索できるツールです。

- **双方向リンク・グラフビュー：** ノートの中で `[[プロジェクトA]]` と書くと、そのノートから「プロジェクトA」というノートへリンクが張れます。さらに、リンク先のノートには「どこから自分が参照されているか」が自動で一覧されます（＝バックリンク）。**グラフビュー**では、ノート同士のつながりが図になって表示されるので、どのノートが重要な「ハブ」になっているかがひと目で分かります。フォルダの階層だけではできない、「関連からたどる検索」が得意です。
- **ノートの整理のやり方：** 有名な方法をそのまま使えます。**Zettelkasten**（1ノート1テーマ＋リンクでつなぐ）、**PARA**（プロジェクト・領域・リソース・アーカイブの4つに分ける）、**MOC（Maps of Content）**（あるテーマのノート一覧をまとめた「目次ノート」）などを、フォルダやタグ、**Dataview**（後述）と組み合わせて運用できます。
- **YAMLフロントマターとDataview：** 各ノートの**いちばん上**に、日付・ステータス・タグなどを書く欄（＝YAMLフロントマター）を置けます。**Dataview**というプラグインを使うと、「未完了のプロジェクトだけ一覧」「今週更新したノート」のように、条件に合うノートを**自動でリストやダッシュボード**にできます（SQLに近いクエリで指定）。
- **注意点：** 設定やプラグインでやりたいことが増えすぎると、「設定いじり」に時間を取られがちです。また、**複数人で同じノートをリアルタイムで同時編集**する機能は標準ではありません。

### **3.2 Google Workspace：クラウドでみんなで同時編集**

**Google Docs・Drive**は、**クラウド上**にドキュメントを置き、複数人が**同じファイルを同時に編集**するのに向いています。コメントや提案モード、変更履歴も使えるので、チームでのフィードバックが速いです。Google DocsはMarkdown対応も進んでおり、見出しや箇条書きをMarkdown風に書くとそのまま装飾されたり、.md形式でエクスポート・インポートしたり、サードパーティの「Docs to Markdown」アドオンで変換したりできます。**「みんなで編集はGoogle Docs、完成版はMarkdownで保存」**というハイブリッド運用も可能です。

### **3.3 ハイブリッド：Google DriveでObsidianのフォルダを同期する場合の注意**

ObsidianのVault（Markdownのフォルダ）を**Google Driveのフォルダ**に置いて、複数デバイスで同じノートを使うやり方もありますが、次の点に気をつけてください。

- **オンデマンド同期（VFS）の問題：** Google Driveなどは「必要なときだけパソコンにダウンロードする」モード（＝オンデマンド同期）があります。この状態だと、ファイルがクラウドにしかないときにObsidianが**リンクや検索を正しく処理できません**。Obsidian用のフォルダは、**「オフラインで使用可能」または「常にこのデバイスに保持」**にし、**常にローカルにコピーがある状態**にしておく必要があります。
- **競合と重複ファイル：** Obsidianは保存が頻繁に走ります。ネットの遅れや、別のデバイスから同時に同じノートを編集すると、Drive側では「どちらを正とするか」を細かくマージできず、**同じ内容の重複ファイル**（例：`Note (1).md`）が静かに増えることがあります。その結果、リンクが別のファイルを指してしまい、ノートのつながりが壊れるリスクがあります。
- **スマホ・タブレット：** スマホ版のGoogle Driveは「パソコンのようなフォルダ」をそのまま見せないため、AndroidではFolderSyncなどのアプリで手動同期、iOSではRemotely SaveやiCloudを使うケースがありますが、**意図しない上書きや古い版に戻る**リスクがあります。
- **重要ルール：** **Obsidianの公式同期（Obsidian Sync）と、Google Drive（またはiCloud）のフォルダ同期は、同時に使わないでください。** 二つの仕組みが同じファイルを同時に更新しようとすると、ループや取り返しのつかない破損の原因になります。

---

## **4. AIを活用した開発手法：バイブコーディング**

### **4.1 バイブコーディングとは何か**

**バイブコーディング（Vibe Coding）**は、**「プログラミングの文法をあまり知らなくても、AIに日本語や英語で指示するだけで、Webサイトやアプリのコードを書かせることができる」**開発のやり方です。つまり、「コードを自分で書く速さ」がボトルネックだったのが、「何を作りたいかをきちんと決めて、設計する力」がボトルネックに移ってきている、という変化です。

注意点もあります。**「AIに任せっぱなし」で進めると、後から直しづらい脆いコードや、将来の修正コストが膨らむ「技術的負債」がたまりやすい**です。そのため、**事前に要件や設計を固めること**と、**AIが生成したコードを人間が必ず確認すること**、そしてAIを「魔法の杖」ではなく「とても強い開発アシスタント」として扱うことが大切です。

### **4.2 会社で導入したときの効果（ROI）とリスク**

バイブコーディングを組織で使うと、以下のような数値が出ている事例があります。

| 指標カテゴリ | 何を測るか（KPI） | どのくらい変わったか | ビジネスへの意味 |
| :---- | :---- | :---- | :---- |
| コスト | 開発・運用コスト | 28%削減 | 定型作業をAIに任せ、人の手を減らせる |
| スピード | リリースまでの時間 | 35%短縮 | 最小限の製品（MVP）を数ヶ月→数日で出せる。PDCAが速く回る |
| マーケ | 顧客獲得単価（CPA） | 28%削減 | ランディングページなどを非エンジニアが自分で作れる |
| 営業 | 見込み客→商談の転換率 | 22%向上 | ダッシュボードや顧客対応AIを素早く作れる |

一方で**「隠れた技術的負債」**に注意が必要です。AIが作ったコードをきちんとレビューせず、全体の設計（アーキテクチャ）も管理しないまま進めると、**絡み合った読みにくいコード（スパゲッティコード）**が増え、後から直すのに多額の費用（事例では約20万ドル）がかかったケースもあります。そのため、**「作った量」だけでなく、設計の一貫性・リリース後の不具合率・レビュー時間**など、新しい評価の物差しを導入することが求められています。

### **4.3 どんなツールを使うか（推奨の流れ）**

- **Google Anti-Gravity：** **これから始める人向け**の学習・試作用です。VS Code（＝よく使われるコード編集ソフト）の上で動き、「タスクを自然言語で渡すと、複数のAIがコードを書いたりターミナルを実行したりブラウザで確認したりする」環境です。まだベータ版で不安定な面もあるので、**本番の基盤というより、プロトタイプや練習用**として使うのがおすすめです。
- **Cursor：** **本格的に開発するときの中心**になるツールです。VS Codeをベースにしているので、拡張機能やショートカットがそのまま使えます。**Tab completion**（次のコードをAIが補完）、**Composer**（複数ファイルをまとめて変更するエージェント機能）が統合されています。料金は Free / Pro（月$20） / Business（1ユーザーあたり$40） / Ultra（$200）など。**クレジット制**なので、高性能モデルを多用すると枠が早く尽きることがあります。**Agent Mode**（AIが自律的に何度も推論するモード）は、枠を超えると従量課金になる場合があります。
- **Claude Code：** **「AIが主役で動き、人があとから確認する」**タイプのツールで、**CLI**（＝黒い画面のコマンドライン）で動きます。長い文脈を効率よく扱え、**トークン**（＝AIが処理するテキストの単位）の消費が少ないという報告があります（同じ作業でCursorの約1/5.5のトークンで済んだ例）。その代わり、**5時間ごとの利用枠**や**週の稼働時間の上限**など、厳しい制限があります。利用規約も厳しくなっており、悪用防止や第三者のツール経由での利用制限があります。**大きなプロジェクトの整理（リファクタリング）や設計の分析**に向いた、やや上級者向けのツールです。
- **FigmaとMCP：** 画面デザイン（UI）を作るなら**Figma**が業界標準です。**Figma Make**で、プロンプトやFigma上のデザインから本番に近いコードを生成できます。**Code to Canvas**と**MCP**（＝AIと外部ツールをつなぐ規格）の連携で、**コードで作った画面をFigmaに取り込んで編集し、またコードに反映する**といった双方向のやりとりができるようになっています。

---

## **5. コードを書かせる前にやること：要件定義と「頼み方」のコツ**

AIにコードを書かせるとき、**いきなり「作って」と頼むと、思っていたのと違うものができたり、何度もやり直しになったり**します。そのため、**何を作りたいかを先に整理する**ことと、**AIへの指示（プロンプト）の仕方を工夫する**ことが重要です。

### **5.1 4段階で「要件」を固める（4-Chat Workflow）**

コードを書き始める**前**に、ChatGPTやClaudeなどのチャットで、次の4段階を踏んで要件を固めることをおすすめします。

1. **ブレインストーミング** — やりたいこと・困っていることをAIに投げ、AIからの質問で「何が本当に欲しいか」をはっきりさせる。  
2. **PRD（製品要件定義書）** — 「誰向けか」「主な機能は何か」「ユーザーがどう動くか」を文章にまとめる。  
3. **TRD（技術要件定義書）** — どんな技術（言語・DBなど）を使うか、データの形、起きうるエラーや例外への対処、セキュリティの前提を書く。  
4. **レビュー** — ここまでで書いた内容に矛盾や抜けがないか、AIに批判的な目で見直してもらう。

こうすると、AIに渡す**文脈（コンテキスト）**がはっきりし、**手戻り**や**ハルシネーション**（AIが事実と違うことを言うこと）を減らしやすくなります。

### **5.2 プロンプトを「部品」で組み立てる（Prompt Lego）**

毎回ゼロから長い指示を書くのは大変なので、**役割・文脈・名前のルール**の3つを意識してプロンプトを組み立てるやり方です。

- **Role（役割）：** 「あなたは一流企業のシニアエンジニアで、曖昧なときは推測せず質問する。保守しやすさと信頼性を重視する」のように、**AIにどんな立場で答えてほしいか**を最初に指定する。  
- **Context（文脈）：** **そのコードがプロジェクトのどこで使われるか**、**どんな価値を生むか**を、毎回短くでいいので伝える。  
- **Naming（命名）：** ボタンや入力欄、関数の**名前のルール**をあらかじめ決めておく。あとで「この部分を直して」と頼むときに、AIも人間も同じものを指しやすくなります。

### **5.3 もう一歩踏み込んだ「頼み方」**

- **プロンプトチェーン：** 大きな目標を**小さなステップに分けて**、一つずつAIに頼む。前のステップの答えを、次のステップの入力に使う（例：まずDBの設計→次にAPI→その次に画面の通信、という順）。  
- **自己洗練・自己批判：** AIに「今出したコードに脆弱性や無駄がないか自分で点検し、問題があれば修正版を出して」と頼む。  
- **動的コンテキスト注入：** 必要な情報を全部プロンプトに書き込むのではなく、**「このエラーに関係しそうなファイルを自分で検索してから直して」**のように、AIに必要な情報をそのときどき取りに来させるやり方です。

---

## **6. ゼロから実務レベルまで：12ヶ月の学びの道のり**

プログラミング未経験でも、以下の4段階で約1年かけて「AIと一緒に実務レベルの開発ができる」状態を目指すロードマップです。

### **フェーズ1：まず「AIに作らせる」体験を積む（1〜3ヶ月）**

- **使うツール：** Google Anti-Gravity（無料ベータ）。  
- **やること：** インストールと初期設定のあと、**データベースを使わない静的なもの**（自分用ポートフォリオ、簡単な計算機、ストップウォッチなど）を週1個ペースで作ってみる。その前に**4-Chat Workflow**で「何を作るか」を文章で整理する練習をする。あえて曖昧な指示を出して、**エラーが出たときにAIがどう動くか**を観察し、「デバッグ（不具合を直す）の大切さ」を体感する。

### **フェーズ2：本番に近い環境で「頼み方」を磨く（4〜6ヶ月）**

- **使うツール：** Cursor（Proプラン）。  
- **やること：** 開発環境（＝IDE）をCursorに統一し、**Prompt Lego**（Role・Context・Naming）を意識して指示する癖をつける。**ログインやダッシュボード表示**のように、**状態**（誰がログインしているか、何を表示するか）を扱う機能に挑戦する。**エラーが出たら、AIにその場で直させるだけにせず、Gitでひとつ前の状態に戻して、プロンプトを書き直してからもう一度やる**「マイクロコミット」の習慣をつける。

### **フェーズ3：デザインとコードを往復させる（7〜9ヶ月）**

- **使うツール：** Cursor、Figma。  
- **やること：** Figmaで**「これが正解の画面」**（ゴールデンスクリーン）を一つ作り、フォント・色・余白のルールを決める。それをAIへの**参照元**にする。MCPでFigmaとCursorやClaude Codeをつなぎ、**「このデザインのこのコンポーネントを使って」**のように具体的に指示する。**Code to Canvas**で、コードからできた画面をFigmaに取り込み、デザインを直してからまたコードに反映する、という**双方向のやりとり**に慣れる。

### **フェーズ4：大きなコードベースと「技術的負債」と向き合う（10〜12ヶ月）**

- **使うツール：** Claude Code、Cursor（両方使う）。  
- **やること：** **CLI**（コマンドライン）でClaude Codeを動かし、AIにファイルの参照・変更を任せて、**大規模な整理（リファクタリング）**に挑戦する。**動的コンテキスト注入**で、必要なファイルだけをAIに渡すようにし、トークンや利用制限を節約する。**新機能を追加する前に、その機能が満たすべきテストを先にAIに書かせ、テストが通るまでAIに自分で直させる**流れを習慣化し、長く持つコードベースにしていく。

---

## **7. よくある失敗パターンと、会社で使うときのルール**

### **7.1 バイブコーディングでやりがちな「落とし穴」**

| 陥りやすいパターン | なぜまずいか | どうすればよいか |
| :---- | :---- | :---- |
| **一度に全部作らせる** | 一つのプロンプトで「全部の機能を作って」と頼むと、つじつまが合わず、あとから直せないコードになりやすい | **小さく分ける**。一つの機能（または一つの画面の流れ）が動いてデザインも合ってから、次に進む「少しずつ作る」やり方を徹底する |
| **デザインをAI任せにする** | AIが出した「なんとなくきれいな画面」で満足し、**使いやすさ（UX）**や操作の順序を人間が考えなくなる | 「この要素は本当に必要か」「操作の流れは自然か」と**自分で問いかけ**、AIを「優秀だけど文脈を忘れるインターン」のように導く |
| **「デザインの統一はあとで」と先送りする** | 色・余白・コンポーネントのルールや、ロード中・エラー時などの**状態**を後回しにすると、あとから直すのがとても大変になる | **最初の「正解画面」（ゴールデンスクリーン）の段階**から、ルールと状態をプロンプトにきちんと書き、それに合わせて作っていく |

### **7.2 会社で導入するとき：セキュリティと「誰が何を使うか」のルール**

- **Google Workspace：** **SSO**（1回ログインで複数サービスに入れる仕組み）や、**アクセス権の一括管理**、退職者のアカウント停止がしやすいです。セキュリティ分析のソフトと組み合わせれば、不正ログインやサードパーティ連携による情報漏洩のリスクを監視できます。  
- **Obsidian（ローカルファースト）：** 会社全体で「一つのナレッジベース」にするには、共有ドライブや**Git**を使ったDocs-as-Codeの運用が必要になります。**開発部門以外**（人事・営業・法務など）に、Gitの概念やコンフリクトの解き方を強く求めると、**「怖くて更新しない」**となり、情報が古いままになる事例があります。一方、**機密や研究データ**を扱う部門では、**データをクラウドに出さず、社内のパソコン内だけに置く**（＝エアギャップに近い運用）ことで、クラウド経由の攻撃や外部AIにデータが渡るリスクを避けられる、という利点があります。

---

## **8. まとめ：何を選び、どう進めるか**

- **Markdown**は、特定のサービスに縛られない（ベンダーロックインの排除）、データを自分のものとして持てる（データ主権）、自動ビルドやAI（RAG）との相性の良さから、**どの編集ソフトを使う場合でも、ナレッジ管理の土台**としておすすめです。  
- **Obsidian**は、個人や研究者・開発者が**ノート同士をリンクでつなぎ、深く考えを広げる**ことや、**自分のメモをAIに読ませて対話する（ローカルRAG）**のに向いています。**Google Docs**は、技術が得意でない人も含めた**チームでの同時編集**と、導入のしやすさで強みがあります。**「みんなで書く・直すのはGoogle Docs、完成したらMarkdownに変換して保存」**というハイブリッドが現実的です。ObsidianをGoogle Driveで同期する場合は、オンデマンド同期・競合・スマホ同期のリスクを理解したうえで使い、可能であれば**Obsidian Sync**や**Git**による信頼性の高い同期を検討してください。  
- **バイブコーディング**は、非エンジニアでも**実用的なアプリをこれまでにない速さで作れる**可能性があります。ただし、「プロンプトを投げて待つだけ」では不十分です。このレポートの**12ヶ月ロードマップ**に沿って、Anti-Gravityで体験→Cursorで本格化→Figmaと連携→Claude Codeで大規模対応、と**段階的にステップアップ**するのがおすすめです。会社で使う場合は、**「作る速さ」だけでなく、技術的負債や設計の一貫性、リリース後の不具合**を見る**ルールや指標（ガバナンス）**を整えることが大切です。  
**「何を作りたいかを論理的に決める力」**と**「品質を妥協しない姿勢」**を保ち、AIを適切に使いこなすことで、個人も組織も、コスト削減とスピードで大きな変化を実現できるでしょう。

---

#### **引用文献**

**【バイブコーディング・開発ツール】**  
1. 2026 AI Business Predictions - PwC, https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-predictions.html  
2. Vibe Coding 2026: What Developers & Businesses Must Know - NanoByte Technologies, https://www.nanobytetechnologies.com/Blog/Vibe-Coding-2026-What-Developers-Businesses-Must-Know-Before-Embracing-AI-Driven-Development  
3. Vibe Coding Tips For Startups - Salesforce, https://www.salesforce.com/blog/vibe-coding-tips-for-startups/  
4. How to Become an AI Engineer in 2026 - KDnuggets, https://www.kdnuggets.com/how-to-become-an-ai-engineer-in-2026-a-self-study-roadmap  
5. Vibe coding is not the same as AI-Assisted engineering - Addy Osmani, Medium, https://medium.com/@addyosmani/vibe-coding-is-not-the-same-as-ai-assisted-engineering-3f81088d5b98  
6. Top 7 Udemy Courses to Learn AI and Vibe Coding in 2026 - Soma, Medium, https://medium.com/javarevisited/top-7-udemy-courses-to-learn-ai-and-vibe-coding-in-2026-8b45a5ac5bf0  
7. Vibe Coding 2026 Cost Savings - Webfries, https://www.webfries.com/blog/vibe-coding-2026-cost-savings/  
8. AI Coding Productivity Statistics 2026 - Panto AI, https://www.getpanto.ai/blog/ai-coding-productivity-statistics  
9. Google Antigravity Developer Tool - Reddit r/AISEOInsider, https://www.reddit.com/r/AISEOInsider/comments/1qi80ta/google_antigravity_developer_tool_the_future_of/  
10. Google Anti-Gravity: The New AI Coding Platform - Reddit, https://www.reddit.com/r/AISEOInsider/comments/1plaz68/google_antigravity_the_new_ai_coding_platform/  
11. Has anyone tried Antigravity by Google? - Reddit r/google, https://www.reddit.com/r/google/comments/1p10ev8/has_anyone_tried_antigravity_by_google_thoughts/  
12. Build $10,000 AI 3D Websites (Google Anti-Gravity Full Tutorial) - YouTube, https://www.youtube.com/watch?v=DJMsXSr1jec  
13. Cursor AI Pricing 2026 - GamsGo, https://www.gamsgo.com/blog/cursor-pricing  
14. Cursor AI Pricing Explained - LowCode Agency, https://www.lowcode.agency/blog/cursor-ai-pricing  
15. Claude Code vs Cursor: Which AI Coding Tool Is Best in 2026? - Kanerika, https://kanerika.com/blogs/claude-code-vs-cursor/  
16. Cursor vs Claude Code: A Comprehensive Comparison - DevTools Academy, https://www.devtoolsacademy.com/blog/cursor-vs-claudecode/  
17. Cursor AI Review 2026 - NxCode, https://www.nxcode.io/resources/news/cursor-review-2026  
18. Cursor · Pricing, https://cursor.com/pricing  
19. Clarifying our pricing (June 2025) - Cursor, https://cursor.com/blog/june-2025-pricing  
20. Claude Code vs Cursor: What to Choose in 2026 - Builder.io, https://www.builder.io/blog/cursor-vs-claude-code  
21. Introducing Claude Sonnet 4.6 - Anthropic, https://www.anthropic.com/news/claude-sonnet-4-6  
22. Claude Code Limits: Quotas & Rate Limits Guide - TrueFoundry, https://www.truefoundry.com/blog/claude-code-limits-explained  
23. Usage Policy Update - Anthropic, https://www.anthropic.com/news/usage-policy-update  
24. Anthropic clarifies ban on third-party tool access to Claude - The Register, https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access/  
25. 10 Best Vibe Coding Tools for Designers in 2026 - Toools.design, https://www.toools.design/blog-posts/vibe-coding-tools-for-designers  
26. Figma's MCP Server Can Now Write to the Canvas - growthmethod.com, https://growthmethod.com/figma-mcp-server/  
27. AI News Digest Feb 2026 - The Neuron, https://www.theneuron.ai/ai-news-digests/around-the-horn-digest-february-2026/  
28. Figma's "Code to Canvas" Will Change Lives - YouTube, https://www.youtube.com/watch?v=kt3M51G1IIw  
29. generate_figma_design not available in Claude Code connector? - Figma Forum, https://forum.figma.com/report-a-problem-6/generate-figma-design-not-available-in-claude-code-connector-51173  
30. Claude Code to Figma Is a Genuine Leap Forward - shyamal, Medium, https://medium.com/@dharshyamal/claude-code-to-figma-is-a-genuine-leap-forward-its-just-not-ready-for-your-design-team-yet-4d0bdba24b7c  
31. Getting started with Vibe-coding (Beginner's guide) - Rajan Dube, Medium, https://medium.com/@rajandube/getting-started-with-vibe-coding-beginners-guide-add1b4803296  
32. I tried vibe coding for 4 weeks - Reddit r/vibecoding, https://www.reddit.com/r/vibecoding/comments/1nu8s3y/i_tried_vibe_coding_for_4_weeks_heres_why_im/  
33. 5 Prompt Components that 10x My Vibe Coding Workflow - Reddit r/vibecoding, https://www.reddit.com/r/vibecoding/comments/1l8c4u2/5_prompt_components_that_10x_my_vibe_coding/  
34. Level up your vibe-coding: A non-engineer's guide - Rosie Dent-Spargo, Medium, https://medium.com/@rosie.dent-spargo/level-up-your-vibe-coding-a-non-engineers-guide-to-engineering-coding-tools-a25099c7fe48  
35. 5 Advanced Prompt Engineering Techniques - GoInsight.AI, https://www.goinsight.ai/blog/advanced-prompt-engineering/  
36. Effective context engineering for AI agents - Anthropic, https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents  
37. The Complete Vibe Coding Guide for Designers (2026) - Muzli Blog, https://muz.li/blog/the-complete-vibe-coding-guide-for-designers-2026/

**【Markdown・ナレッジ管理・RAG】**  
38. Building a Markdown-Based Documentation System - Rost, Medium, https://medium.com/@rosgluk/building-a-markdown-based-documentation-system-72bef3cb1db3  
39. Markdown: Is it The Future of Online Documentation? - Axiata Digital Labs, https://www.axiatadigitallabs.com/2024/12/16/markdown-is-it-the-future-of-online-documentation/  
40. Empowering Developers with Markdown-based Documentation - IBM Research, https://research.ibm.com/publications/empowering-developers-with-markdown-based-documentation-for-better-software-maintenance  
41. Best Documentation Tools for 2025 - Typemill, https://typemill.net/knowledge-hub/best-documentation-tools  
42. Google Docs vs Obsidian (2026) - YouTube, https://www.youtube.com/watch?v=4dKpsywXK3o  
43. Do you use Git and Markdown in your documentation process? - Reddit r/technicalwriting, https://www.reddit.com/r/technicalwriting/comments/1kx98cp/do_you_use_git_and_markdown_in_your_documentation/  
44. Can Google Docs replace Obsidian as my second brain? - androidpolice.com, https://www.androidpolice.com/google-docs-replace-obsidian-as-second-brain/  
45. Technical Writers Rejoice: Full Markdown Interoperability Coming to Google Docs, upcurvecloud.com, https://upcurvecloud.com/blog/technical-writers-rejoice-full-markdown-interoperability-coming-to-google-docs/  
46. How Markdown heats up AI - HackMD, https://hackmd.io/@hackmd-blog/markdown-heats-up-ai-2025  
47. Docs as Code - Write the Docs, https://www.writethedocs.org/guide/docs-as-code.html  
48. Thoughts on Docs as code being a broken promise - Idratherbewriting.com, https://idratherbewriting.com/blog/thoughts-on-docs-as-code-promise  
49. Docs as code doesn't have to mean Markdown and Git - Andrew Owen, https://andrewowen.net/blog/docs-as-code-doesnt-have-to-mean-markdown-and-git/  
50. HackMD vs Google Docs - HackMD, https://hackmd.io/@hackmd-blog/hackmd-vs-google-docs-choosing-right-tool-for-your-workflow  
51. Do you use any knowledge management? - Reddit r/ExperiencedDevs, https://www.reddit.com/r/ExperiencedDevs/comments/1pwb67r/do_you_use_any_knowledge_management/  
52. Be honest! How useful are bi-directional links? - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/12tczl2/be_honest_how_useful_are_bidirectional_links/  
53. Folders vs. linking vs. tags—the definitive guide - Obsidian Forum, https://forum.obsidian.md/t/folders-vs-linking-vs-tags-the-definitive-guide-extremely-short-read-this/78468  
54. My Note-taking System or Zettelkasten for Devs - DEV Community, https://dev.to/pkorsch/my-note-taking-system-or-zettelkasten-for-devs-f28  
55. PARA vs Zettelkasten vs MOC - YouTube, https://www.youtube.com/watch?v=zlQfHWDYuGI  
56. MOCs Vs Zettelkasten: An 80/20 approach - Obsidian Forum, https://forum.obsidian.md/t/mocs-vs-zettelkasten-an-80-20-approach-for-those-of-us-who-arent-luhmann/106518  
57. Taking advantage of orderly PARA and chaotic Zettelkasten - Obsidian Forum, https://forum.obsidian.md/t/taking-advantage-of-orderly-para-and-chaotic-zettelkasten-methodologies-simultaneously/47786  
58. obsidian - Skill | Smithery, https://smithery.ai/skills/fgarofalo56/obsidian  
59. Markdown Cheatsheet in Obsidian - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1iwb3fh/markdown_cheatsheet_in_obsidian/  
60. markdown-journal-rust: RAG to index md files - GitHub, https://github.com/estevaom/markdown-journal-rust  
61. obsidian-vault-management-skill - playbooks.com, https://playbooks.com/skills/julianobarbosa/claude-code-skills/obsidian-vault-management-skill  
62. [Feature]: Dynamic Kanban board - obsidian-kanban GitHub, https://github.com/mgmeyers/obsidian-kanban/issues/345  
63. Writing a Novel in Markdown with Obsidian - pdworkman.com, https://pdworkman.com/writing-a-novel-in-markdown/  
64. Advantages of Obsidian vs google docs for non-power user - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1acshv6/advantages_of_obsidian_vs_google_docs_for/  
65. Google Expands Markdown Support in Docs, Slides, and Drawings - Thurrott.com, https://www.thurrott.com/cloud/305632/google-expands-markdown-support-in-docs-slides-and-drawings  
66. Use Markdown in Google Docs, Slides, & Drawings - Google Support, https://support.google.com/docs/answer/12014036?hl=en  
67. Docs™ to Markdown - Google Workspace Marketplace, https://workspace.google.com/marketplace/app/docs_to_markdown/700168918607  
68. Recommended workflow for structured exporting from Obsidian TO Google Docs? - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1pqoqj6/recommended_workflow_for_structured_exporting/  
69. Obsidian to google doc - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1c4xfx0/obsidian_to_google_doc/  
70. Mastering Your Knowledge Base: Sync Obsidian With Google Drive, explore.st-aug.edu, https://explore.st-aug.edu/exp/mastering-your-knowledge-base-the-definitive-guide-to-sync-obsidian-with-google-drive  
71. Syncing Obsidian via One Drive / Google Drive between Android and PC - Reddit, https://www.reddit.com/r/ObsidianMD/comments/1f78vf9/syncing_obsidian_via_one_drive_google_drive/  
72. Sync your notes across devices - Obsidian Help, https://help.obsidian.md/sync-notes  
73. Best Practices for Obsidian Sync with OneDrive - Reddit, https://www.reddit.com/r/ObsidianMD/comments/1inikjk/best_practices_for_obsidian_sync_with_onedrive/  
74. How to deal with duplicate files created by sync - Obsidian Forum, https://forum.obsidian.md/t/how-to-deal-with-duplicate-files-created-by-sync/83075  
75. Editor: Add a toggle to disable automatic merging - Obsidian Forum, https://forum.obsidian.md/t/editor-add-a-toggle-to-disable-automatic-merging-of-changes-non-obsidian-sync/14874  
76. Computers as I used to love them - Hacker News, https://news.ycombinator.com/item?id=29837696  
77. What are issues with using Google Drive to sync? - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1hszxao/what_are_issues_with_using_google_drive_to_sync/  
78. A reliable (and free) way to sync Windows and iOS - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1p8qpj1/a_reliable_and_free_way_to_sync_windows_and_ios/  
79. Obsidian sync and Google drive - Obsidian Forum, https://forum.obsidian.md/t/obsidian-sync-and-google-drive/76762  
80. Sync conflicts with Google Drive + Obsidian Sync? - Obsidian Forum, https://forum.obsidian.md/t/sync-conflicts-with-google-drive-obsidian-sync/108275  
81. Boosting AI Performance: The Power of LLM-Friendly Content in Markdown - developer.webex.com, https://developer.webex.com/blog/boosting-ai-performance-the-power-of-llm-friendly-content-in-markdown  
82. Optimizing Content for AI - BYU-Idaho, https://td.byui.edu/TDClient/79/ITHelpCenter/KB/ArticleDet?ID=16822  
83. Why Markdown is the Secret Weapon for Document AI - Kevin Wang, Medium, https://medium.com/@hlcwang/why-markdown-is-the-secret-weapon-for-document-ai-b3fd517a101b  
84. Markdown: From 2004 to the AI Era - NicFab Blog, https://www.nicfab.eu/en/posts/markdown-sense/  
85. Writing for AI. Writing Guide for LLM and RAG - Ragina Jeon, Medium, https://lyingdragon.medium.com/writing-for-ai-caab3344f279  
86. Yet another RAG system - Reddit r/LocalLLaMA, https://www.reddit.com/r/LocalLLaMA/comments/16cbimi/yet_another_rag_system_implementation_details_and/  
87. Best Chunking Strategies for RAG in 2025 - Firecrawl, https://www.firecrawl.dev/blog/best-chunking-strategies-rag-2025  
88. RAG in Generative AI: The Definitive 2025 Masterclass - Psitron, https://psitrontech.com/blog/rag-in-generative-ai-the-definitive-2025-masterclass  
89. RAG for AI memory: why is everyone indexing databases instead of markdown files? - Reddit r/Rag, https://www.reddit.com/r/Rag/comments/1r2hlzd/rag_for_ai_memory_why_is_everyone_indexing/  
90. Metadata-Driven Retrieval-Augmented Generation for Financial QA - arXiv, https://arxiv.org/html/2510.24402v1  
91. From Markdown to Memory: How I Organized My Brain for AI - Fabian, Medium, https://medium.com/@fhennek/from-markdown-to-memory-how-i-organized-my-brain-for-ai-79b13dfe95cc  
92. Obsidian AI Agent with the Google Gemini Scribe Plugin - effortlessacademic.com, https://effortlessacademic.com/obsidian-ai-agent-with-the-google-gemini-scribe-plugin-for-academics/  
93. Have you tried using AI tools like NotebookLM or Gemini in Obsidian? - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1lie7x0/have_you_tried_using_ai_tools_like_notebooklm_or/  
94. Neural Composer: Local Graph RAG (LightRAG) - Obsidian Forum, https://forum.obsidian.md/t/neural-composer-local-graph-rag-made-easy-lightrag-integration/109891  
95. Why Gemini 1.5 (and other large context models) are bullish for RAG - Medium, https://medium.com/enterprise-rag/why-gemini-1-5-and-other-large-context-models-are-bullish-for-rag-ce3218930bb4  
96. The Long Context RAG Capabilities of OpenAI o1 and Google Gemini - Databricks Blog, https://www.databricks.com/blog/long-context-rag-capabilities-openai-o1-and-google-gemini  
97. Thoughts on Gemini 2.5 Pro and large documents - Reddit r/Rag, https://www.reddit.com/r/Rag/comments/1k9mqy0/thoughts_on_gemini_25_pro_and_its_performance/  
98. Switching over from Google Docs? - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1pepz49/switching_over_from_google_docs/  
99. Is obsidian good for company knowledge base? - Reddit r/ObsidianMD, https://www.reddit.com/r/ObsidianMD/comments/1kouo8o/is_obsidian_good_for_company_knowledge_base/  
100. Top Security Analytics Software for Google Workspace in 2025 - Slashdot, https://slashdot.org/software/security-analytics/for-google-workspace/  
101. Obsidian Security Expands to Google Cloud Marketplace, https://www.obsidiansecurity.com/blog/obsidian-security-expanded-reach-to-google-cloud-marketplace  
102. AI That Knows You - Obsidian Forum, https://forum.obsidian.md/t/ai-that-knows-you/73892  
103. Obsidian Vs Google Docs 2026 - YouTube, https://www.youtube.com/watch?v=FP5H_rmZG6I  
