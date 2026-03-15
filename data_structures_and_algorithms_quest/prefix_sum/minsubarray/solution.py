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
    def solve(self, nums: List[int], p: int) -> int:
        n = len(nums)
        prefix_mod = [0] * (n + 1)
        for i in range(n):
            prefix_mod[i + 1] = (prefix_mod[i] + nums[i]) % p

        r = prefix_mod[-1]
        if r == 0:
            return 0

        result = n
        last_seen = {}
        for idx, val in enumerate(prefix_mod):
            target = (val - r) % p
            if target in last_seen:
                result = min(result, idx - last_seen[target])
            last_seen[val] = idx

        return result if result < n else -1


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
