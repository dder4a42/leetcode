#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

import sys
import ast
from typing import List, Optional, Tuple, Any
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Solution:
    @auto_io
    def solve(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        cnt = defaultdict(int)
        local = 0
        div = 0
        res = 0

        for i in range(k):
            local += nums[i]
            cnt[nums[i]] += 1
        
        if len(cnt) >= m:
            res = local
        div = len(cnt)
        for i in range(k, n):
            local = local - nums[i-k] + nums[i]
            if cnt[nums[i]] == 0:
                div += 1
                
            cnt[nums[i-k]] -= 1
            cnt[nums[i]] += 1

            if cnt[nums[i-k]] == 0:
                div -= 1

            if div >= m:
                res = max(res, local)

        return res


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
