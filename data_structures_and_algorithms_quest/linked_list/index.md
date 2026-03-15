# linked_list

> INDEX_FORMAT_V1

| slug | title | leetcode | solution | code | analysis_anchor |
| --- | --- | --- | --- | --- | --- |
| odd_even_list | Odd Even Linked List | https://leetcode.com/problems/odd-even-linked-list/ | - | ./odd_even_list/solution.py | odd_even_list |
| reverse_list | Reverse Linked List | https://leetcode.com/problems/reverse-linked-list/ | - | ./reverse_list/solution.py | reverse_list |

## 题目分析

### odd_even_list
将奇偶位置节点拆分后再拼接。
- 遍历过程中维护奇链与偶链；
- 最后将奇链表尾部连接到偶链表头部。

### reverse_list
原地反转链表：一次遍历，逐步把当前节点头插到新链表前端。

### 其他
删除升序链表中的重复元素：快慢指针即可，注意边界条件。