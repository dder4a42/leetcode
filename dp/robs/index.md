# 打家劫舍

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| cycle_rob | House Robber II | https://leetcode.cn/problems/house-robber-ii/ | - | ./cycle_rob/solution.py | cycle_rob |
| count_house_placements | Count House Placements | https://leetcode.cn/problems/count-number-of-ways-to-place-houses/description/ | - | ./count_house_placements/solution.py | count_house_placements |

## 题目分析

### cycle_rob

在环形数组上，num[0] 和 nums[-1] 是相邻元素，不能同时选取，则可分类讨论 nums[0:-2] 和 nums[1:-1]

### count_house_placements

由于街道两侧互不干扰，可以仅仅计算一侧的方案数，最后平方取模即可。

若希望同时考虑两侧，也可以设状态 00, 01, 10, 11 为都不放置，放置一侧，都放置