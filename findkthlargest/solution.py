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
    def solve(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest element using three-way quickselect.
        Handles duplicates efficiently with O(n) average, O(n^2) worst-case.
        """
        n = len(nums)
        target_idx = n - k  # Convert kth largest to (n-k)th smallest
        return self.quickselect(nums, 0, n-1, target_idx)

    def quickselect(self, nums: list[int], left: int, right: int, target_idx: int) -> int:
        """
        Three-way quickselect algorithm.
        Returns the element at position target_idx in sorted order.
        """
        if left == right:
            return nums[left]

        # Random pivot to avoid worst-case on sorted arrays
        pivot_idx = random.randint(left, right)
        pivot = nums[pivot_idx]

        # Three-way partition: | < pivot | = pivot | > pivot |
        # Use Dutch National Flag algorithm
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

        if target_idx < i:
            return self.quickselect(nums, left, i-1, target_idx)
        elif target_idx >= j:
            return self.quickselect(nums, j, right, target_idx)
        else:
            # target_idx falls within pivot equal range
            return pivot

def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
