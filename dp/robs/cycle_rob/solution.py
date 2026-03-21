from typing import List, Optional, Tuple, Any

from utils import ListNode, TreeNode, auto_io, with_types, run_tests

class Solution:
    @auto_io
    def solve(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1]) 

        dp = [0] * (n-1)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        res = dp[-1]

        dp = [0] * (n-1)
        dp[0] = nums[1]
        dp[1] = max(dp[0], nums[2])

        for i in range(3, n):
            dp[i-1] = max(dp[i-2], dp[i-3] + nums[i])
        
        res = max(res, dp[-1])

        return res


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
