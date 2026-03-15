#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

from typing import List, Optional, Tuple, Any

from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Solution:
    @auto_io
    def solve(self, numbers: List[int], target: int) -> List[int]:
        lh, rh = 0, len(numbers)-1
        while lh < rh:
            if numbers[lh]+numbers[rh] < target:
                lh += 1
            elif numbers[lh]+numbers[rh] > target:
                rh -= 1
            else:
                return [lh+1, rh+1]
        raise ValueError("lh eqaul to rh")
            


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
