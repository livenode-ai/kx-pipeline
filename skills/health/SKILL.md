---
name: health
description: Vault健康診断。スキーマ準拠・孤児ノート・リンク健全性・マップバランスの4項目をチェック。「/health」「ヘルスチェック」で発動。
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
---

# /health — Vault 健康診断

notes/ の構造的健全性を4項目でチェックする。月次メンテナンス用。

---

## 実行

`/health` で全4項目を実行。結果を `ops/health/YYYY-MM-DD-report.md` に保存する。

---

## 診断 1: スキーマ準拠

notes/ の全 .md ファイル（マップファイルを除く）について:

```bash
for f in notes/*.md; do
  [[ -f "$f" ]] || continue
  # マップファイルは除外
  grep -q '^type: moc' "$f" && continue
  # frontmatter存在チェック
  head -1 "$f" | grep -q '^---$' || echo "FAIL: $f — frontmatterなし"
  # 必須フィールド
  grep -q '^description:' "$f" || echo "WARN: $f — description欠落"
  grep -q '^topics:' "$f" || echo "WARN: $f — topics欠落"
  grep -q '^type:' "$f" || echo "WARN: $f — type欠落"
  grep -q '^domain:' "$f" || echo "WARN: $f — domain欠落"
done
```

| 状態 | レベル |
|------|--------|
| frontmatterなし | FAIL |
| 必須フィールド欠落 | WARN |
| 全ノート合格 | PASS |

---

## 診断 2: 孤児ノート

他のファイルから1つもリンクされていないノートを検出する。

```bash
for f in notes/*.md; do
  [[ -f "$f" ]] || continue
  grep -q '^type: moc' "$f" && continue
  basename=$(basename "$f" .md)
  count=$(grep -rl "\[\[$basename\]\]" --include='*.md' . 2>/dev/null | grep -v "$f" | wc -l | tr -d ' ')
  if [[ "$count" -eq 0 ]]; then
    echo "ORPHAN: $f — 被リンク 0"
  fi
done
```

| 状態 | レベル |
|------|--------|
| 7日以上の孤児 | FAIL |
| 7日以内の孤児 | WARN（接続待ち） |
| 孤児なし | PASS |

---

## 診断 3: リンク健全性

全ファイルの `[[リンク先]]` が実在するファイルを指しているか。

```bash
grep -roP '\[\[([^\]]+)\]\]' --include='*.md' . | sed 's/.*\[\[//;s/\]\].*//' | sort -u | while read target; do
  found=$(find . -name "$target.md" -not -path "./.git/*" 2>/dev/null | head -1)
  if [[ -z "$found" ]]; then
    echo "DANGLING: [[$target]]"
    grep -rl "\[\[$target\]\]" --include='*.md' . 2>/dev/null | head -5
  fi
done
```

| 状態 | レベル |
|------|--------|
| ダングリングリンクあり | FAIL |
| 全リンク解決 | PASS |

---

## 診断 4: マップバランス

各ドメインマップに登録されているノート数を数える。

```bash
# Auto-detect domain maps (files ending in -map.md in notes/)
for mapfile in notes/*-map.md; do
  map=$(basename "$mapfile" .md)
  count=$(grep -rl "\[\[$map\]\]" notes/ --include='*.md' 2>/dev/null | wc -l | tr -d ' ')
  echo "$map: $count notes"
done
```

| 状態 | レベル |
|------|--------|
| マップに5件未満 | WARN（過疎） |
| マップに50件超 | WARN（分割検討） |
| 5-50件 | PASS |

---

## レポート出力

```markdown
# Health Report — YYYY-MM-DD

Notes: N | Maps: N (auto-detected) | Inbox: N

## Summary: N FAIL, N WARN, N PASS

### [1] スキーマ準拠 ... PASS/WARN/FAIL
[詳細]

### [2] 孤児ノート ... PASS/WARN/FAIL
[詳細]

### [3] リンク健全性 ... PASS/WARN/FAIL
[詳細]

### [4] マップバランス ... PASS/WARN/FAIL
[詳細]

---

## 推奨アクション（上位3件）
1. [最も影響の大きいアクション]
2. [次に重要なアクション]
3. [3番目のアクション]
```

レポートを `ops/health/YYYY-MM-DD-report.md` に保存する。

---
