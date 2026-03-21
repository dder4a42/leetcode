#!/usr/bin/env python3
"""
LeetCode Problem: Container With Most Water
"""

from typing import List

from utils import auto_io, run_tests


class Solution:
    @auto_io
    def solve(self, height: List[int]) -> int:
        n = len(height)
        lh, rh = 0, n - 1
        ans = 0
        while lh < rh:
            ans = max(ans, min(height[lh], height[rh]) * (rh - lh))

            if height[lh] < height[rh]:
                lh += 1
            else:
                rh -= 1

        return ans


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
