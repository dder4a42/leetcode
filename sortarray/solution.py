#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

import sys
import ast
from typing import List, Optional, Tuple, Any
from pathlib import Path
import random

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Solution:
    @auto_io
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.Qs(nums, 0, n-1)
        return nums

    def Qs(self, nums,left,right):
        if left >= right:
            return  # Base case: subarray has 0 or 1 element

        # Random pivot selection
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]

        # Three-way partition (Dutch National Flag)
        i, j, m = left, left, right

        while j <= m:
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > pivot:
                nums[j], nums[m] = nums[m], nums[j]
                m -= 1
            else:
                j += 1

        # After partition:
        # nums[left:i] < pivot
        # nums[i:j] = pivot
        # nums[j:right+1] > pivot

        # Recursively sort left and right regions
        self.Qs(nums, left, i - 1)
        self.Qs(nums, j, right)

def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
