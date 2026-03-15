#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

import sys
from typing import List, Optional, Tuple, Any


class Solution:
    def solve(self, input_data: str) -> str:
        """
        Main solver function.
        Implement your algorithm here.

        Args:
            input_data: Raw input string for a single test case

        Returns:
            Solution as a string
        """
        heights = [int(x) for x in input_data.split(" ")]

        # Single-pass monotonic stack solution
        stack = []  # each element: (start_index, height)
        max_area = 0
        n = len(heights)

        for i in range(n):
            start = i
            # Pop bars higher than current, calculate their areas
            while stack and stack[-1][1] >= heights[i]:
                j, h = stack.pop()
                # Width from start index j to i-1, so width = i - j
                max_area = max(max_area, h * (i - j))
                start = j  # extend start to the popped index
            stack.append((start, heights[i]))

        # Process remaining bars in stack
        while stack:
            j, h = stack.pop()
            # Width from j to end, so width = n - j
            max_area = max(max_area, h * (n - j))

        return str(max_area)


def parse_test_cases(filename: str = "test_cases.txt") -> List[Tuple[str, str]]:
    """
    Parse test cases from file.
    Expected format:
      Line 1: Input
      Line 2: Expected Answer
      Line 3: Blank line (separator)
    Returns list of (input, expected_answer) tuples.
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

        # Read input line
        input_line = lines[i]
        i += 1

        # Skip empty lines between input and expected
        while i < len(lines) and not lines[i].strip():
            i += 1

        if i >= len(lines):
            break

        # Read expected answer line
        expected_line = lines[i]
        i += 1

        test_cases.append((input_line, expected_line))

        # Skip blank line separator
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

    for i, (input_data, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"  Input:    {input_data}")
        print(f"  Expected: {expected}")

        try:
            result = solution.solve(input_data)
            print(f"  Output:   {result}")

            # Normalize for comparison (strip whitespace)
            if str(result).strip() == str(expected).strip():
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
