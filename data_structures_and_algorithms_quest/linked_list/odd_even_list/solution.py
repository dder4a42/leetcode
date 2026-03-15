#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

import sys
import ast
from typing import List, Optional, Tuple, Any
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Double_ListNode:
    def __init__(self, val=-1, pre=None, suc=None):
        self.val = val
        self.pre = pre
        self.suc = suc


class Solution:
    @auto_io
    def solve(self, head: ListNode) -> ListNode:
        """
        Main solver function.
        Implement your algorithm here.

        Args:
            head: ListNode - head of the linked list

        Returns:
            ListNode: head of the reordered linked list
        """
        # if not head or not head.next:
        #     return head

        # odd_head, even_head = head, head.next
        # odd_current, even_current = odd_head, even_head

        # while even_current and even_current.next:
        #     odd_current.next = even_current.next
        #     odd_current = odd_current.next
        #     even_current.next = odd_current.next
        #     even_current = even_current.next

        # odd_current.next = even_head
        # return odd_head

        # 使用一个双向节点 pivot 兼任 odd list 的尾指针和 even list 的头指针
        # 不断取出 odd node 并插入至 pivot 前
        if head == None:
            return None
        if head.next == None or head.next.next == None:
            return head

        pivot = Double_ListNode(-1, head, head.next)
        head.next = pivot
        pivot.pre = head
        current = pivot.suc
        while current and current.next:
            tmp = current.next
            current.next = tmp.next
            pivot.pre.next = tmp
            tmp.next = pivot
            pivot.pre = tmp
            current = current.next

        pivot.pre.next = pivot.suc
        return head


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
