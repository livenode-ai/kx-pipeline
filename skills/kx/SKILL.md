---
name: kx
description: KXパイプライン。00_Inbox/のソースをnotes/の構造化ノートに精錬する。掘削→接続→遡及→検査→索引更新の5フェーズを1コマンドで実行。「/kx」「精錬して」「process inbox」で発動。
user-invocable: true
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# /kx — Knowledge Transformation Pipeline

00_Inbox/ のソースを notes/ の構造化ノートに精錬する一発コマンド。
KX = Knowledge Transformation。原鉱から精錬まで、全工程を1回で回す。

---

## 実行

**対象: $ARGUMENTS**

- 引数なし or "inbox" → 00_Inbox/ の全 .md ファイルを処理
- ファイル名指定 → そのファイルだけ処理
- `--quick` → Phase 3（遡及）をスキップ

---

## Phase 1: スキャン

00_Inbox/ の .md ファイルを列挙する。PDF・.DS_Store は除外。
空なら「Inbox is empty」で終了。

```
Found N files in inbox. Starting KX pipeline.
```

---

## Phase 2: 掘削（旧 /process）

各ソースファイルを読み、独立したアイデア・インサイト・意思決定を**全て**個別ノートとして抽出する。

### 抽出の原則

**Mining（掘削）であり Summarizing（要約）ではない。**
ソースの中にある独立した知見を1つ残らず掘り出す。「たぶん知ってる」「当たり前すぎる」はスキップ理由にならない。

判断基準: 「未来のセッションがこれを検索可能なノートとして持っていたら助かるか？」→ YES なら抽出。

### 抽出する対象

- 独立したアイデア・インサイト（1ノート = 1アイデア、アトミック）
- 意思決定とその理由
- 後で調べるべき問い
- 人・組織・プロジェクト間の接続
- アクションアイテム → capture in your preferred task manager（ノートにはしない）

### ノートスキーマ

```yaml
---
description: "タイトルを補足する1文（最大200文字）。メカニズム・スコープ・含意を書く"
type: idea | insight | decision | question | tension | synthesis
# domains are defined in livenode-kx.config.yaml
domain: [your-domain-1 | your-domain-2 | ...]
created: YYYY-MM-DD
language: ja | en | mixed
relevant_notes: []
topics: []
---
```

### タイトルルール

タイトルは**主張**にする。ラベルではない。
- NG: 「リモートワーク」
- OK: 「リモートワークは深い集中時間を構造的に生み出せる」
- テスト: `since [[タイトル]]` で文が成立するか？

### Noetic Cell構造（insight, decision, synthesis タイプは必須）

```markdown
## 主張（Claim）
核心の主張を1-2文で。

## 根拠（Evidence）
なぜそう言えるか。ロジック・定性的理由。

## データ（Data）
定量データ・表・出典付きファクト。
※ 出典は [機関/著者, 年, タイトル] で統一
※ データがない場合はこのセクション省略可

## 制約（Constraints）
この主張が成り立つ条件・限界。
※ 元ソースに明示されている制約のみ。AIが推論で補わない

## 接続（Links）
関連ノートへの [[wikilink]] と関係性（extends / grounds / contradicts / exemplifies）
```

idea, question タイプは 主張 + 接続 のみで可。

### 品質ゲート（書く前に確認）

1. タイトルが主張になっているか？
2. description がタイトルにない情報を追加しているか？
3. domain が最低1つあるか？
4. topics にドメインマップのリンクが最低1つあるか？
5. 本文がタイトルの繰り返しではなく発展しているか？
6. insight/decision/synthesis → 主張 + 接続セクションがあるか？

### ソースの処理

ノート抽出後、ソースファイルを configurable archive path（configurable）に移動する。

---

## Phase 3: 接続（旧 /connect）

Phase 2 で作成した全ノートについて、既存ノートとの接続を探す。

### 手順

1. 作成したノートの domain を確認
2. 該当するドメインマップ（domain maps defined in livenode-kx.config.yaml）を読む
3. マップ内の既存ノートと新ノートの関連を探す
4. **クロスドメイン接続を特に重視**（your-domain-1 ↔ your-domain-2 等）
5. 接続が見つかったら：
   - 新ノートの `## 接続（Links）` に [[既存ノート]] を追加
   - 既存ノートの `## 接続（Links）` にも [[新ノート]] を追加（双方向）
   - ドメインマップに新ノートを追加
6. 関係性は必ず理由を書く。「関連」ではダメ。「extends: ○○の論を△△に拡張」のように

---

## Phase 4: 遡及（旧 /revisit）— `--quick` 時はスキップ

新ノートの作成によって影響を受ける**既存の古いノート**を選び、接続を更新する。

### 候補の選定

- Phase 3 で接続先になった既存ノートのうち、接続数が少ないもの（限界接続価値が高い）を3-5件選ぶ
- Phase 3 の結果が少ない場合: 新ノートと同じドメインマップのノートから接続数が少ないものを選ぶ

### 更新内容

- 古いノートの `## 接続（Links）` に新ノートへのリンクを追加
- description が古くなっていたら改善（ただし主張は変えない）
- 古いノートのタイトルが主張になっていなければフラグを立てる（修正はしない、報告のみ）

---

## Phase 5: 検査（旧 /check）

Phase 2-4 で作成・更新した全ノートの品質を最終確認する。

### チェック項目

1. **スキーマ**: frontmatter の必須フィールド（description, type, domain, created, topics）が揃っているか
2. **タイトル**: 主張になっているか
3. **description**: タイトルの言い換えになっていないか
4. **マップ登録**: 少なくとも1つのドメインマップに登録されているか
5. **接続**: 最低1つの他ノートへのリンクがあるか

問題があるノートはレポートに列挙するが、パイプラインはブロックしない。

---

## Phase 6: 索引更新

notes/CLAIMS_INDEX.md を再生成する。

全ノートの `## 主張（Claim）` セクション（なければタイトル）を1行ずつ集約する。

```markdown
# CLAIMS_INDEX

| ノート | 主張 |
|--------|------|
| [[ノートタイトル]] | 主張の1-2文 |
```

---

## 最終レポート

```
## KX Complete

- ソース処理: N件
- ノート作成: N件
- ノート接続: N件（クロスドメイン: M件）
- 既存ノート遡及: N件
- 品質チェック: PASS / N件の問題あり

### 作成ノート
- [[タイトル]] — type — 1行サマリー

### 発見した接続
- [最も興味深いクロスドメイン接続]

### 次のアクション
- [処理中に発見したタスク]
```

---

## エラー処理

- 特定ファイルで失敗 → スキップして続行。最終レポートで報告
- 接続が見つからないノート → 正常。全ノートがすぐ接続されるわけではない
- 品質チェックで問題 → 列挙するがブロックしない
