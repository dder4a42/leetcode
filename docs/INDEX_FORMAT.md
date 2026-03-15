# 子目录 index.md 规范（INDEX_FORMAT_V1）

目标：让每个题型目录（如 hash、mono_stack、double_ptr）都能被脚本稳定解析，并自动汇总到根目录 index.md。

## 1) 文件结构

建议每个子目录的 index.md 使用以下结构：

```markdown
# <topic_name>

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| two_sum | Two Sum | https://leetcode.com/problems/two-sum/ | ./two_sum/README.md | ./two_sum/solution.py | two_sum |

## 题目分析

### two_sum
用哈希表记录需求值，在遍历时检查当前值是否命中。
```

## 2) 字段定义

- slug：题目目录名（必须与实际文件夹同名）
- title：题目标题（中英文均可）
- leetcode：题目 URL（可填 `-`）
- solution：本地题解文档路径（相对当前子目录，可填 `-`）
- code：代码路径（相对当前子目录，通常是 `./<slug>/solution.py`）
- analysis_anchor：分析段锚点（可填 `-`），用于根目录跳转到本文件中的分析文字

## 3) 约束

- 支持 5 列（兼容旧格式）或 6 列（含 analysis_anchor）。
- `slug` 必须唯一。
- `code` 建议始终填写，便于跳转。
- 未完成内容统一用 `-` 占位。
- 若 `analysis_anchor` 为空，脚本会尝试自动匹配标题 `### <slug>`。

## 4) 示例

```markdown
# hash

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| two_sum | Two Sum | https://leetcode.com/problems/two-sum/ | - | ./two_sum/solution.py | two_sum |
| copy_randomlist | Copy List with Random Pointer | https://leetcode.com/problems/copy-list-with-random-pointer/ | - | ./copy_randomlist/solution.py | copy_randomlist |

## 题目分析

### two_sum
哈希一次遍历，空间换时间。

### copy_randomlist
两次遍历，第一遍建映射，第二遍连 random 指针。
```
