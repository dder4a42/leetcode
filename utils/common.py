#!/usr/bin/env python3
"""
Common data structures for LeetCode problems.
Includes ListNode and TreeNode definitions.
"""


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        current = self
        while current:
            vals.append(str(current.val))
            current = current.next
        return f"ListNode([{','.join(vals)}])"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        while self and other:
            if self.val != other.val:
                return False
            self = self.next
            other = other.next
        return self is None and other is None


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        if self.val != other.val:
            return False
        return (self.left == other.left) and (self.right == other.right)
