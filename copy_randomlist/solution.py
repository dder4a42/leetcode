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


class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


test_list = Node(-1)
test_list.random = test_list


def parse_random_list(data):
    """
    Parse nested list format [[val, random_idx], ...] to Node linked list.
    Each element is [value, random_index] where random_index is:
      - integer: index of node to point random pointer to
      - None: random pointer is None
    """
    if not data or len(data) == 0:
        return None

    nodes = []
    for item in data:
        if not isinstance(item, list) or len(item) == 0:
            return None
        val = item[0]
        if val is None:
            return None
        nodes.append(Node(val))

    for i in range(len(nodes)):
        if nodes[i] and i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if nodes[i] and data[i] and len(data[i]) > 1:
            random_idx = data[i][1]
            if random_idx is not None and 0 <= random_idx < len(nodes):
                nodes[i].random = nodes[random_idx]

    return nodes[0] if nodes else None


def serialize_random_list(head):
    """
    Serialize Node linked list to [[val, random_idx], ...] format.
    """
    if not head:
        return []

    nodes = []
    node_map = {}
    index = 0
    current = head

    while current:
        node_map[current] = index
        index += 1
        current = current.next

    current = head
    while current:
        random_idx = None
        if current.random:
            random_idx = node_map.get(current.random)
        nodes.append([current.val, random_idx])
        current = current.next

    return nodes


class Solution:
    @auto_io
    def solve(self, head: List) -> List:
        """
        Main solver function.
        Implement your algorithm here.

        Input: List in format [[val, random_idx], [val, random_idx], ...]
        Output: Deep copy of the linked list with correct random pointers
        """

        parsed = parse_random_list(head)
        if not parsed:
            return []

        h = {}
        new_head = Node(parsed.val, None, None)
        current = parsed.next
        new_current = new_head
        h[parsed] = new_head

        while current:
            new_current.next = Node(current.val, None, None)
            new_current = new_current.next
            h[current] = new_current
            current = current.next

        current = parsed
        new_current = new_head
        while current:
            if current.random:
                new_current.random = h[current.random]
            current = current.next
            new_current = new_current.next

        return serialize_random_list(new_head)


def main():
    """Main entry point."""
    solution = Solution()
    run_tests(solution)


if __name__ == "__main__":
    main()
