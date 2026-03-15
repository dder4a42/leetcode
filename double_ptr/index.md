# double_ptr

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| twosum_ii | Two Sum II - Input Array Is Sorted | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ | - | ./twosum_ii/solution.py | twosum_ii |

## 题目分析

### twosum_ii
头尾双指针相向移动：和小于 target 时左指针右移，和大于 target 时右指针左移。
利用有序性可保证不遗漏唯一解。