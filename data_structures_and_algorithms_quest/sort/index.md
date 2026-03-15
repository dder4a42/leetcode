# sort

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| find_k-th_largest | Kth Largest Element in an Array | https://leetcode.com/problems/kth-largest-element-in-an-array/ | - | ./find_k-th_largest/solution.py | find_k-th_largest |
| insertion_sort_list | Insertion Sort List | https://leetcode.com/problems/insertion-sort-list/ | - | ./insertion_sort_list/solution.py | insertion_sort_list |
| reductionoperations | Reduction Operations to Make the Array Elements Equal | https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/ | - | ./reductionoperations/solution.py | reductionoperations |
| sort_array | Sort an Array | https://leetcode.com/problems/sort-an-array/ | - | ./sort_array/solution.py | sort_array |

## 题目分析

### find_k-th_largest
Top K 经典做法：
- 全排序后取第 $k$ 大；
- 维护大小为 $k$ 的最小堆；
- QuickSelect / 三路划分，只递归目标侧子问题。

### insertion_sort_list
链表插入排序：
- 用 `dummy` 统一头插边界；
- 每次把当前节点插入到有序部分的正确位置。

### reductionoperations
将问题转化为排序后“分层下降”的累积步数问题，贪心累加每层需要的操作次数。

### sort_array
可使用快速排序、归并排序或堆排序实现通用数组排序。