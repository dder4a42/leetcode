# double_ptr

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| twosum_ii | Two Sum II - Input Array Is Sorted | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ | - | ./twosum_ii/solution.py | twosum_ii |
| container_with_most_water | Container With Most Water | https://leetcode.com/problems/container-with-most-water/ | - | ./container_with_most_water/solution.py | container_with_most_water |

## 题目分析

### twosum_ii

头尾双指针相向移动：和小于 target 时左指针右移，和大于 target 时右指针左移。
利用有序性可保证不遗漏唯一解。

若暴力枚举 (i, j)，则搜索空间为二维，可以列为上三角矩阵，且由升序数组的条件，满足：

+ i 增大时，和递增
+ j 增大时，和递增

故而可利用单调性剪枝，将 (0, n-1) 作为枚举起点，

+ 若和大于 target，则 j 所在列均被排除
+ 若和小于 target，则 i 所在行均被排除

由于 i，j 只会单向移动，可以保证我们总是更接近解。

### container_with_most_water

同样的二维搜索空间，相向双指针。这里的盛水量为`min(h[i], h[j]) * (j-i)`

+ 宽度可以随 i，j 的靠近而缩短
+ min 函数单调不增

第二点指的是，对 $i<k<j,h[i]<h[j]$，有

$$
\min(h[i], h[k]) \le \min(h[i], h[j])
$$

利用该单调性进行剪枝。