# prefix_sum

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| minsubarray | Make Sum Divisible by P | https://leetcode.com/problems/make-sum-divisible-by-p/ | - | ./minsubarray/solution.py | minsubarray |
| waystomakefair | Ways to Make a Fair Array | https://leetcode.com/problems/ways-to-make-a-fair-array/ | - | ./waystomakefair/solution.py | waystomakefair |

## 题目分析

### minsubarray
移除最短子数组，使剩余和能被 $p$ 整除。
核心是把区间和写成前缀和之差，并在模意义下用哈希表查找目标余数。

### waystomakefair
维护奇偶下标前缀和。删除一个位置后，右侧元素奇偶性翻转，
据此在 $O(n)$ 内判断每个删除点是否可使奇偶和相等。