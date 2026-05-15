# livenode-kx

> AIに知識ではなく、判断軸を渡す。

AIメモリーが覚えるのは「あなたが知っていること」。
livenode-kx が保存するのは「あなたがどう判断するか」。

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blueviolet)](https://claude.ai/code)
[![English](https://img.shields.io/badge/lang-English-blue.svg)](README.md)

**[コンテキスト約85%削減](docs/concepts.md#1-noetic-cell) · 5分でセットアップ · Obsidian・Logseq・任意のMarkdownフォルダで動作**

> *削減率は、500ノート規模のVaultで2行のClaimセクションのみを読む場合と、約50行のノート全文を読む場合を比較した推定値です。計算方法は [concepts.md](docs/concepts.md) を参照。*

---

## livenode-kx とは？

livenode-kx は、Claude Code 向けの 4コマンド構成の Knowledge Transformation パイプラインです。

ボイスメモやメモ書きを `00_Inbox/` に放り込み、`/kx` を実行すると、構造化されたナレッジグラフ ── 50行のノート全文ではなく2行のClaimセクションだけをAIに読ませる Noetic Cell ノート ── が返ってきます。セッションの終わりに `/distill` を実行すれば、あなたが下した判断はすべて `BRIEFING.md` に蓄積され、次のセッションは完全なコンテキスト付きで始まります。これを続けると、AIは汎用的な出力を出さなくなり、あなたの思考様式に合わせた出力を返すようになります。

**Obsidian・Logseq・任意のMarkdownフォルダで動作します。独自フォーマットはありません。あなたのノートはあなたのものです。**

---

## 解決したい問題

あなたのナレッジは既にある。AIはそれを取り出せる。

しかし、検索（retrieval）はAIに「なぜあなたがその選択をするのか」を伝えません ── 何を受け入れ、何を却下し、自分のドメインでトレードオフをどう推論するか。そのため出力は80〜90%は正しく、残りを修正することにあなたの時間が溶けます。

その修正時間は、スキル不足ではありません。構造的な欠落です ── AIは「あなたが何を知っているか」にはアクセスできても、「あなたがどう判断するか」にはアクセスできない。livenode-kx は、あなたの判断軸を永続化しアクセス可能にすることで、この欠落を埋めます。

---

## どう動くか

ほとんどのAIメモリーツールは2層構造です：

```
[あなたのノート] ─────────────────────→ [LLM]
                  セマンティック距離           汎用的な出力
```

livenode-kx は、欠落している判断軸レイヤーを追加します：

```
[あなたのノート / 外部ナレッジベース]
         │
         ▼
┌─────────────────────────────┐
│   判断軸レイヤー             │  ← livenode-kx
│                             │
│  • 構造化された主張          │
│    （Noetic Cell・段階読み） │
│  • 判断の履歴                │
│    （BRIEFING.md）           │
│  • YES/NOパターン            │
│    （AESTHETIC.md）          │
│  • アクティブな文脈          │
│    （CLAIMS_INDEX）          │
└─────────────────────────────┘
         │
         ▼
    [LLMの出力]
    あなたの推論に合わせて校正されている
```

mem0、MemGPT、Zep のようなツールは「あなたが何を知っているか」── 検索（retrieval）── を解いています。livenode-kx は「あなたがどう判断するか」── 判断軸（judgment）── を解いています。両者は競合ではなく補完関係にあります。

---

## ライフサイクル ── 4コマンドはループで初めて価値を生む

`/kx` と `/distill` は単発ツールではありません。**判断軸が蓄積される循環構造の対の半分**です。

```
                ┌──────────────────────────────────┐
                │                                  │
   ① セッションで判断する                          │
        │                                          │
        ▼                                          │
   ② /distill                                      │
       HOを 00_Inbox/ に書き出す                    │
       BRIEFING / VISION / AESTHETIC / MEMORY を    │
       差分更新                                     │
        │                                          │
        ▼                                          │
   ③ /kx                                           │
       00_Inbox/ の HO を Noetic Cell ノートへ精錬  │
       notes/ にアトミックに保存                    │
       CLAIMS_INDEX を再構築                        │
        │                                          │
        ▼                                          │
   ④ 次のセッションで /ref                          │
       CLAIMS_INDEX を起点に段階読み                │
       過去の判断軸をフルコンテキストでロード        │
        │                                          │
        └──────────────────────────────────────────┘
                    ① へ戻る
```

**ループが回って初めて「AIが判断軸を持つ」状態が生まれます。** `/distill` だけ回しても HO が溜まるだけ。`/kx` だけ回しても判断履歴が入ってこない。両方を毎セッション回すことで、ノートが構造化されたあなたの判断軸として蓄積されていきます。

各ファイルの置き場所（BRIEFING.md / VISION.md / AESTHETIC.md / MEMORY.md）は `livenode-kx.config.yaml` の `distill:` セクションで調整できます。デフォルトは Vault 直下、PARA運用なら `01_Projects/{project}/BRIEFING.md` のようなパターンに変更可能です。

---

## 4つのコマンド

| コマンド | 役割 |
|---|---|
| `/kx` | 生の入力 → 構造化された Noetic Cell ノート（5フェーズのパイプライン） |
| `/distill` | セッション → ハンドオーバー → BRIEFING更新 → AESTHETICキャリブレーション |
| `/health` | 月次Vault健康診断：スキーマ・孤児ノート・リンク健全性・マップバランス |
| `/ref` | CLAIMS_INDEX による段階読み ── 500ノートを数秒で俯瞰 |

---

## クイックスタート

**前提：** [Claude Code](https://claude.ai/code) がインストール・認証済み · Markdown のVaultディレクトリがある

### TL;DR（3ステップ）

```bash
cp -r livenode-kx/skills/ /path/to/your-vault/.claude/skills/
cp livenode-kx/livenode-kx.config.yaml /path/to/your-vault/
cp livenode-kx/templates/CLAUDE.md.template /path/to/your-vault/CLAUDE.md
```

VaultをClaude Codeで開き、`/kx` と打つ。

### 詳細セットアップ（約5分） → [docs/quickstart.md](docs/quickstart.md)

---

## 主要コンセプト

- **[Noetic Cell](docs/concepts.md#1-noetic-cell)** ── なぜ5セクション構造はフラットテキストよりAI検索で優位なのか（85%コンテキスト削減）
- **[Mining vs Summarizing](docs/concepts.md#2-mining-vs-summarizing)** ── `/kx` の背景にある思想
- **[判断軸レイヤー](docs/architecture.md)** ── 3層アーキテクチャの詳細

---

## Vault互換性

| 環境 | サポート |
|---|---|
| Obsidian Vault | ✅ フル（ローカルファイル操作） |
| Obsidian + MCP | ✅ config の `obsidian_mcp: true` で有効化 |
| 任意のMarkdownフォルダ | ✅ フル |
| Logseq | ✅ 動作（フラットMarkdownモード） |
| Cloudflare Artifacts | 🔜 近日対応予定 |

---

## コントリビューション

[.claude/rules/contributing.md](.claude/rules/contributing.md) を参照してください。

不変条件： **スキルはVault非依存でなければならない。** 絶対パス・ユーザー名・ドメイン名のハードコードは禁止。

---

## ライセンス

MIT © livenode-kx contributors
