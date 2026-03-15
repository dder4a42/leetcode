#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

from typing import List, Optional, Tuple, Any

from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Solution:
    @auto_io
    def solve(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1, head)
        current = head
        while current and current.next:
            tmp = current.next
            p = dummy
            while p.next != tmp and p.next.val < tmp.val:
                p = p.next
            
            if p != current:
                current.next = tmp.next
                tmp.next = p.next
                p.next = tmp
            else:
                current = current.next
        return dummy.next


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
