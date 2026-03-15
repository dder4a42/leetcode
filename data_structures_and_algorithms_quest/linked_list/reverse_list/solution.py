#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

import sys
import ast
from typing import List, Optional, Tuple, Any
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils import ListNode, TreeNode, auto_io, with_types


class Solution:
    @auto_io
    def solve(self,  head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Main solver function.
        Implement your algorithm here.

        Type Hints for auto_io:
            Replace '...' with your parameters and types:
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
        if head == None or head.next == None:
            return head

        dummy_head = ListNode(-1, head)
        current = head.next
        while current:
            head.next = current.next
            current.next = dummy_head.next
            dummy_head.next = current
            current = head.next

        return dummy_head.next


def parse_test_cases(filename: str = "test_cases.txt") -> List[Tuple[List[str], Any]]:
    """
    Parse test cases from file.
    Expected format:
      Line 1: First input line
      Line 2: Second input line (optional, can have multiple lines)
      ...
      Line N: "---" (separator line)
      Line N+1: Expected Answer (Python literal - e.g., 9, "[0,1]", "[[1,2],[1,4]]")
      Blank line separator between test cases
    
    Returns list of (input_args, expected_answer) tuples where input_args is a list of strings.
    """
    test_cases = []
    try:
        with open(filename, 'r') as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

    i = 0
    while i < len(lines):
        # Skip comments and empty lines at the start
        while i < len(lines) and (lines[i].strip().startswith('#') or not lines[i].strip()):
            i += 1

        if i >= len(lines):
            break

        # Collect input lines until we hit "---" separator
        input_args = []
        while i < len(lines) and lines[i].strip() != "---" and not lines[i].strip().startswith('#'):
            if lines[i].strip():  # Skip empty lines within input
                input_args.append(lines[i].strip())
            i += 1

        # Skip the "---" separator line
        if i < len(lines) and lines[i].strip() == "---":
            i += 1

        if i >= len(lines):
            break

        # Skip empty lines between input and expected
        while i < len(lines) and not lines[i].strip():
            i += 1

        if i >= len(lines):
            break

        # Read expected answer line
        expected_line = lines[i]
        i += 1
        
        # Parse expected answer as Python literal
        try:
            expected_answer = ast.literal_eval(expected_line)
        except (SyntaxError, ValueError):
            # If not valid Python literal, keep as string
            expected_answer = expected_line

        test_cases.append((input_args, expected_answer))

        # Skip blank line separator between test cases
        while i < len(lines) and not lines[i].strip():
            i += 1

    return test_cases


def run_tests():
    """
    Run all test cases from test_cases.txt and print results.
    Shows PASS/FAIL for each test case.
    """
    solution = Solution()
    test_cases = parse_test_cases()

    if not test_cases:
        print("No test cases found in test_cases.txt")
        print("\nPlease add test cases in the format:")
        print("  input_line")
        print("  expected_answer")
        print("  (blank line separator)")
        return

    passed = 0
    failed = 0

    print("=" * 60)
    print(f"Running {len(test_cases)} test case(s)")
    print("=" * 60)

    for i, (input_args, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"  Input:    {input_args}")
        print(f"  Expected: {expected}")

        try:
            result = solution.solve(*input_args)
            print(f"  Output:   {result}")

            # Compare Python objects directly
            if result == expected:
                print(f"  Status:   [PASS]")
                passed += 1
            else:
                print(f"  Status:   [FAIL]")
                failed += 1

        except Exception as e:
            print(f"  Error:    {e}")
            print(f"  Status:   [FAIL]")
            failed += 1
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 60)
    print(f"Results: {passed} passed, {failed} failed out of {len(test_cases)}")
    print("=" * 60)


def main():
    """Main entry point."""
    run_tests()


if __name__ == "__main__":
    main()
