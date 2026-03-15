#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

import sys
import ast
from typing import List, Optional, Tuple, Any
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Solution:
    @auto_io
    def solve(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n+1)
        for i in range(n+1):
            for j in range(i+1, min(i+4, n+1)):
                if dp[j] == 0:
                    dp[j] = dp[i] + costs[j-1] + (j-i) ** 2
                else:
                    dp[j] = min(dp[j], dp[i] + costs[j-1] + (j-i) ** 2)
        
        return dp[n]


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
