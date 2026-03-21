from typing import List, Optional, Tuple, Any

from utils import ListNode, TreeNode, auto_io, with_types, run_tests

class Solution:
    @auto_io
    def solve(self, n: int) -> int:
        dp = [1] * 4
        p = 1000_000_007
        for i in range(n-1):
            tmp = [0] * 4

            tmp[0] = sum(dp) % p
            tmp[1] = (dp[2] + dp[0]) % p
            tmp[2] = (dp[1] + dp[0]) % p
            tmp[3] = dp[0] % p

            dp = tmp
        return sum(dp) % p


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
