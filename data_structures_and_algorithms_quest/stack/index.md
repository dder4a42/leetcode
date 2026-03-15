# stack

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| exclusiveTime | Exclusive Time of Functions | https://leetcode.com/problems/exclusive-time-of-functions/ | - | ./exclusiveTime/solution.py | exclusivetime |

## 题目分析

### exclusivetime
维护函数调用栈与上一次时间戳：
- `start` 时先给栈顶函数补上运行时间，再入栈新函数；
- `end` 时弹栈并累计当前函数区间，更新上次时间戳。