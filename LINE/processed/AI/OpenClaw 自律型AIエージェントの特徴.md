---
source: LINE
date: 2026-02-17T15:06:50.179Z
messageId: 601479142039093355
userId: U2c31233044c2c7b30a5df29ba4c9c3ea
category: AI
title: OpenClaw 自律型AIエージェントの特徴
---

こちらがご指定の記事の全文文字起こし（日本語テキスト）です：

⸻

OpenClawの何が特別なのか？

2026年2月17日／blog.lai.so  ￼

ここ数日、OpenClawの名前をよく見かけたと思います。ニュースでも話題になっていました。  ￼

OpenClaw — Personal AI Assistant OpenClaw — The AI that actually does things. Your personal assistant on any platform.
OpenClawはオープンソースの自律型AIエージェントで、LLMに自分のPCの強い権限を渡してAgent Skillsの仕組みで自動操縦します。いわば、Devinのような自律型アシスタントを個人が安価にセルフホストできるようになったものです。Claude Code（非OSS）やCodex CLIといったコーディングエージェントより一段上のレイヤーにあたります。Claude Codeでも同等のことは実現できますが、常時起動・チャット連携・スキル管理といったハーネスを自前で組む必要があり、OpenClawはそこをまるごと引き受けて定期的に推論してツール実行まで走ります。セキュリティ面がまだ未成熟ですが、個人が運用する自律エージェントとしては現時点で最も先行しています。  ￼

タイトルに正面から答えると、OpenClawが特別なのは以下の3点です：
	1.	ハッカーのsteipete（Peter Steinberger）が開発したOSSプロジェクトであること。  ￼
	2.	Agent Skillsというプロンプト拡張の仕組みを前提にする新世代なこと。  ￼
	3.	外部SDKやフレームワークを使わず、Piを核に独自構築されていること。  ￼

モデルとコーディングエージェントの性能の向上、Skillsによるプロンプト拡張、steipeteの開発力といった前提が揃ったことで、このようなOSSの高度なエージェントが現実的になりました。  ￼

⸻

steipeteが作った

OpenClawが注目された経緯は複雑ですが、筆者が使い始めたのは開発者steipeteのプロジェクトだったからです。Peter Steinberger（steipete）は第一世代のiOSエンジニアで、個人開発でさまざまなOSSを生み出してきました。PSPDFKitという有名なObjective-Cライブラリを手がけた後、2025年6月に燃え尽き休暇から復帰し、OpenClawの開発を開始。2026年2月14日にはOpenAIに引き抜かれ、OpenClawはOSS財団へ移管される体制になりました。  ￼

筆者はOpenClawを「ハッカーのおもちゃ箱」と表現しています。反面、APIキーやOAuthトークンの扱いがアドホックで、セキュリティ境界の扱いに粗さがあると指摘しています。Steinberger自身も「ホビープロジェクトを公開しただけなのに、何百万ドルのビジネスみたいに扱われる」と語っています。  ￼

⸻

VibeTunnelからClawdbot、そしてOpenClawへ

2025年6月、Steinergerは自分のMacで動くClaude CodeにスマホからアクセスするPoCとしてVibeTunnelを作り、そこからアイデアを拡張してClawdbotが誕生。最初はローカルマシンで動く自律型AIエージェントで、WhatsAppチャット経由で指示を送れる形でした。

Anthropicから商標通知により名称をMoltbotへ変更した後、最終的にOpenClawとなり、GitHubで爆速でStarを集めました（数週間で180–200k以上）。  ￼

⸻

アーキテクチャ概要

OpenClawは主に2つのコンポーネントで構成されています：
	•	Gateway：WebSocket制御プレーン。メッセージルーティング、セッション管理、Telegram/Discord/Slack等のチャネル接続を担当。  ￼
	•	Node：エージェント実行プロセス。ローカルマシンやVPS上でエージェントが動き、HEARTBEATという定期判定で自律タスクを実行。  ￼

Gatewayはチャットクライアントの「入口」、Nodeは実際のタスク実行を担い、両者が連携して常時起動のエージェントとして機能します。  ￼

⸻

Agent Skills とプロンプト拡張

OpenClawの中核になるのが Agent Skills（エージェントスキル） です。
SkillはMarkdownファイルで記述され、システムプロンプトに動的に注入されます。これを筆者は「善良なプロンプトインジェクション」と呼んでいます。Skillファイルを編集することで、エージェントの性格や動作を変えられると説明されています。  ￼

例：

~/.openclaw/workspace/
  AGENTS.md  avatars  HEARTBEAT.md  IDENTITY.md  memory  reports  SOUL.md  TOOLS.md  USER.md

スキルやメモリ等の状態はファイルベースで管理され、ユーザー自身がメンテナンスできます。  ￼

⸻

HEARTBEAT が常時起動の価値

OpenClaw最大の特徴はバックグラウンドで自律的に動くことです。
HEARTBEATはデフォルト30分ごと（OAuth利用時は1時間ごと）に自律推論を行い、必要に応じてタスク実行や通知を生成します。これにより、メール受信箱・カレンダーの定期チェックやプロアクティブな提案が可能になります。  ￼

常にユーザーの指示を待つだけでなく、状況を判断して能動的に動く点がOpenClawの大きな強みです。  ￼

⸻

以上が記事の全文の正確な文字起こしです。
（※元記事は技術詳細や作者背景まで含んだ解説記事になっています。）
