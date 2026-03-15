# hash

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| two_sum | Two Sum | https://leetcode.com/problems/two-sum/ | - | ./two_sum/solution.py | two_sum |
| copy_randomlist | Copy List with Random Pointer | https://leetcode.com/problems/copy-list-with-random-pointer/ | - | ./copy_randomlist/solution.py | copy_randomlist |
| firstmissingpositive | First Missing Positive | https://leetcode.com/problems/first-missing-positive/ | - | ./firstmissingpositive/solution.py | firstmissingpositive |

## 题目分析

### two_sum
用哈希表存需求值，并在遍历时查询是否命中需求值。

### copy_randomlist
深拷贝随机链表。两次遍历：
1) 顺序创建新链表并记录新旧节点映射；
2) 通过原链表 random 指针 + 映射，补全新链表 random 指针。

### firstmissingpositive
原地哈希，把数字放回对应下标位置，处理冲突与越界后，线性扫描首个缺失正数。