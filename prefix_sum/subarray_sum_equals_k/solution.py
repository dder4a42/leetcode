#!/usr/bin/env python3
"""
LeetCode Problem: Subarray Sum Equals K
"""

from collections import defaultdict
from typing import List

from utils import auto_io, run_tests


class Solution:
    @auto_io
    def solve(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        prefix_sum = 0
        ans = 0

        for x in nums:
            prefix_sum += x
            ans += cnt[prefix_sum - k]
            cnt[prefix_sum] += 1

        return ans


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
