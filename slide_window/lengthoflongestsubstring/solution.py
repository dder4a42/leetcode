#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

from typing import List, Optional, Tuple, Any

from utils import ListNode, TreeNode, auto_io, with_types, run_tests


class Solution:
    @auto_io
    def solve(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        
        cnt = set(s[0])
        res = 0
        lh, rh = 0, 1
        while rh < n:
            if s[rh] in cnt:
                while s[lh] != s[rh]:
                    cnt.remove(s[lh])
                    lh += 1
                lh += 1
            else:
                cnt.add(s[rh])
            
            res = max(res, rh - lh + 1)
            rh += 1
        return res


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
