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
    def solve(self, nums: List[int]) -> int:
        """
        Main solver function.
        Implement your algorithm here.

        Type Hints for auto_io:
            Replace '*args' with your parameters and types:
                def solve(self, head: ListNode) -> ListNode:
                def solve(self, root: TreeNode) -> List[int]:
                def solve(self, nums: List[int], target: int) -> List[int]:

        Example - Single ListNode parameter:
            @auto_io
            def solve(self, head: ListNode) -> ListNode:
                return head  # Your logic here

        Example - TreeNode with List[int] return:
            @auto_io
            def solve(self, root: TreeNode) -> List[int]:
                return [1, 2, 3]  # Your logic here

        Available types:
            ListNode, TreeNode, List, int, str, bool, Optional[...]
        """
        n = len(nums)
        prefix_odd, prefix_even = [0], [0]
        for i in range(n):
            if i % 2 == 0:
                prefix_even.append(prefix_even[-1] + nums[i])
            else:
                prefix_odd.append(prefix_odd[-1] + nums[i])
        
        result = 0
        for i in range(n):
            if i % 2 == 0:
                # Remove even-indexed element: elements after i flip parity
                # New odd = old odd (before i) + old even (after i)
                odd = prefix_odd[i // 2] + (prefix_even[-1] - prefix_even[i // 2 + 1])
                # New even = old even (before i, excluding i) + old odd (after i)
                even = prefix_even[i // 2] + (prefix_odd[-1] - prefix_odd[i // 2])
            else:
                # Remove odd-indexed element: elements after i flip parity
                # New odd = old odd (before i) + old even (after i)
                # Note: prefix_odd[i // 2] excludes current element since i is odd
                odd = prefix_odd[i // 2] + (prefix_even[-1] - prefix_even[i // 2 + 1])
                # New even = old even (before i+1, excluding i) + old odd (after i)
                even = prefix_even[i // 2 + 1] + (prefix_odd[-1] - prefix_odd[i // 2 + 1])

            if even == odd:
                result += 1
        return result
            


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
