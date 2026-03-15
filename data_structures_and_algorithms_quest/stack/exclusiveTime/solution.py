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
        # TODO: Implement your solution
        args = input_data.split(" ")
        n = int(args[-1])
        logs = args[:-1]

        result = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            pid, op, timestamp = log.split(":")
            pid, timestamp = int(pid), int(timestamp)

            if op == "start":
                if stack:
                    result[stack[-1]] += timestamp - prev_time
                stack.append(pid)
                prev_time = timestamp
            else:
                result[pid] += timestamp - prev_time + 1
                stack.pop()
                prev_time = timestamp + 1

        return str(result)


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
        with open(filename, "r") as f:
            lines = [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

    i = 0
    while i < len(lines):
        # Skip comments and empty lines at the start
        while i < len(lines) and (
            lines[i].strip().startswith("#") or not lines[i].strip()
        ):
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
