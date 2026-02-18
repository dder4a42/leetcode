#!/usr/bin/env python3
"""
LeetCode Problem: PROBLEM_TITLE
"""

import sys
import ast
import heapq
from typing import List, Optional, Tuple, Any


class Solution:
    def solve(self, *args: str) -> List[List[int]]:
        """
        Main solver function.
        Implement your algorithm here.

        Args:
            *args: Input lines for a single test case
            Expected format: "nums1 = [1,7,11], nums2 = [2,4,6], k = 3"
            or three separate lines

        Returns:
            Solution as a list of lists
        """
        # Handle both single-line and multi-line formats
        if len(args) == 1:
            # Single line format: "nums1 = [1,7,11], nums2 = [2,4,6], k = 3"
            parts = args[0].split(", ")
            nums1_part = parts[0].split("=")[-1].strip()
            nums2_part = parts[1].split("=")[-1].strip()
            k_part = parts[2].split("=")[-1].strip()
        elif len(args) == 3:
            # Multi-line format: three separate lines
            nums1_part = args[0].split("=")[-1].strip()
            nums2_part = args[1].split("=")[-1].strip()
            k_part = args[2].split("=")[-1].strip()
        else:
            raise ValueError(f"Unexpected number of arguments: {len(args)}")

        nums1 = [int(x.strip()) for x in nums1_part[1:-1].split(",")]
        nums2 = [int(x.strip()) for x in nums2_part[1:-1].split(",")]
        k = int(k_part)

        # Both arrays are non-decreasing (sorted)
        # Use min-heap to find k smallest sums
        if not nums1 or not nums2 or k <= 0:
            return []

        result = []
        # Min-heap: (sum, i, j) where i is index in nums1, j is index in nums2
        heap = []

        # Initialize heap with (nums1[i] + nums2[0], i, 0) for first min(k, len(nums1)) elements
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and len(result) < k:
            current_sum, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            # If there's next element in nums2 for same nums1[i], push it
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result


def parse_test_cases(
    filename: str = "test_cases.txt",
) -> List[Tuple[List[str], List[List[int]]]]:
    """
    Parse test cases from file.
    Expected format:
      Input lines (one or more)
      "---" separator line
      Expected Answer (Python list literal)
      Blank line separator between test cases

    Returns list of (input_args, expected_answer) tuples where input_args is a list of strings.
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

        # Collect input lines until we hit "---" separator
        input_args = []
        while (
            i < len(lines)
            and lines[i].strip() != "---"
            and not lines[i].strip().startswith("#")
        ):
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

        # Parse expected answer as Python list
        try:
            expected_answer = ast.literal_eval(expected_line)
        except (SyntaxError, ValueError) as e:
            print(
                f"Warning: Failed to parse expected answer on line {i}: {expected_line}"
            )
            print(f"Error: {e}")
            expected_answer = []

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
        print("  input_line(s)")
        print("  ---")
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

            # Compare list structures directly
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
