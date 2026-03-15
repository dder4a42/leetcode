#!/usr/bin/env python3
"""
LeetCode Problem: First Missing Positive
"""

import sys
import ast
from typing import List, Optional, Tuple, Any
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Solution:
    @auto_io
    def solve(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 2 if nums[0] == 1 else 1

        for i in range(n):
            num = nums[i]
            while num > 0 and num <= n:
                pos = num - 1
                if nums[pos] == num:
                    break
                nums[i], nums[pos] = nums[pos], num
                num = nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
