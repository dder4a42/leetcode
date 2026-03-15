# queue

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| countStudents | Number of Students Unable to Eat Lunch | https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/ | - | ./countStudents/solution.py | countstudents |
| timeRequiredToBuy | Time Needed to Buy Tickets | https://leetcode.com/problems/time-needed-to-buy-tickets/ | - | ./timeRequiredToBuy/solution.py | timerequiredtobuy |

## 题目分析

### countstudents
直接模拟队列可做，但更简洁的是统计两类餐点需求数量，
按栈顶餐点持续消费；当某类需求为 0 且栈顶仍是该类时结束。

### timerequiredtobuy
可由贡献法计算总时间：
- 对于目标位置左侧和自身，最多贡献 `tickets[k]`；
- 对于目标位置右侧，最多贡献 `tickets[k]-1`；
线性累加即可。