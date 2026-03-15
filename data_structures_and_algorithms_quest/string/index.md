# string

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| repeatedSubstringPattern | Repeated Substring Pattern | https://leetcode.com/problems/repeated-substring-pattern/ | - | ./repeatedSubstringPattern/solution.py | repeatedsubstringpattern |

## 题目分析

### repeatedsubstringpattern
利用字符串性质（或 KMP 结论）可快速判断：
- 构造 `t = s + s`，去掉首尾字符后检查是否包含 `s`；
- 若包含，说明 `s` 可由某个子串重复拼接得到。

### 其他
旋转字符串也可借助 `s + s` 覆盖所有循环位移结果，再做包含判断。
