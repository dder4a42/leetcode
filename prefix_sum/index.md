# 前缀和

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| subarray_sum_equals_k | Subarray Sum Equals K | https://leetcode.com/problems/subarray-sum-equals-k/ | - | ./subarray_sum_equals_k/solution.py | subarray_sum_equals_k |

## 题目分析

### subarray_sum_equals_k

若定义左闭右开区间 [i, j)，则子数组的和即为前缀和之差 `sum[j]-sum[i]`。类似两数之和，在遍历到下标 j 时，可以用哈希表查询是否存在 i<j 满足前缀和之差为 k。