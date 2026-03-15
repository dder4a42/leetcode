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


class Solution:
    @auto_io
    def solve(self, nums: List[int], target: int) -> List[int]:
        """
        Main solver function.
        Implement your algorithm here.

        Type Hints for auto_io:
            Replace '*args' with your parameters and types:
                def solve(self, head: ListNode) -> ListNode:
                def solve(self, root: TreeNode) -> List[int]:
                def solve(self, nums: List[int], target: int) -> List[int]:

        Example - Single ListNode parameter:
            @auto_io
            def solve(self, head: ListNode) -> ListNode:
                return head  # Your logic here

        Example - TreeNode with List[int] return:
            @auto_io
            def solve(self, root: TreeNode) -> List[int]:
                return [1, 2, 3]  # Your logic here

        Available types:
            ListNode, TreeNode, List, int, str, bool, Optional[...]
        """
        n = len(nums)
        h = {}
        for i, x in enumerate(nums):
            if x in h:
                return [h[x], i]
            h[target - x] = i


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
