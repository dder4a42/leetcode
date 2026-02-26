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
    def solve(self, nums: list[int]) -> int:
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
        if n == 1:
            return 0

        # Sort the array to process values in ascending order
        nums = sorted(nums)

        stride = 0
        num_stage = 0
        res = 0
        a = nums[0]
        for i in range(n):
            if nums[i] == a:
                stride += 1
                continue
            res += stride * num_stage
            num_stage += 1
            stride = 1
            a = nums[i]

        res += stride * num_stage
        return res


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
