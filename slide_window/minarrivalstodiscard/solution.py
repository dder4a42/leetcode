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
    def solve(self, arrivals: List[int], w: int, m: int) -> int:
        res = 0
        n = len(arrivals)
        cnt = [0] * (n+1)
        for i in range(w):
            cnt[arrivals[i]] += 1

            if cnt[arrivals[i]] > m:
                res += 1
                cnt[arrivals[i]] -= 1
                arrivals[i] = 0

        for i in range(w, len(arrivals)):
            cnt[arrivals[i-w]] -= 1
            cnt[arrivals[i]] += 1

            if cnt[arrivals[i]] > m:
                res += 1
                cnt[arrivals[i]] -= 1
                arrivals[i] = 0

        return res


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
