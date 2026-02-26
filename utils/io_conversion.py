#!/usr/bin/env python3
"""
IO conversion utilities for LeetCode problems.
Handles conversion between serializable types and LeetCode data structures.
"""

import ast
from typing import List, Optional, Any, Union, get_origin, get_args
from collections import deque

from . import ListNode, TreeNode


def list_to_listnode(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def listnode_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


def list_to_treenode(arr: List[int]) -> Optional[TreeNode]:
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
        if node.left:
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
        if node.right:
            queue.append(node.right)
        i += 1
    return root


def treenode_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


def parse_string_to_type(value: str, target_type: type) -> Any:
    if target_type is str:
        return value
    if target_type is int:
        return int(value)
    if target_type is float:
        return float(value)
    if target_type is bool:
        return value.lower() in ("true", "1", "yes")
    return ast.literal_eval(value)


def convert_to_target_type(value: Any, target_type: type) -> Any:
    if get_origin(target_type) is Union:
        args = get_args(target_type)
        for arg in args:
            if arg is not type(None):
                return convert_to_target_type(value, arg)
        return value

    if target_type in (int, float, str, bool):
        if isinstance(value, str):
            return parse_string_to_type(value, target_type)
        return target_type(value)

    if get_origin(target_type) is list:
        if isinstance(value, str):
            value = ast.literal_eval(value)
        return value

    if target_type is ListNode:
        if isinstance(value, str):
            value = ast.literal_eval(value)
        return list_to_listnode(value)

    if target_type is TreeNode:
        if isinstance(value, str):
            value = ast.literal_eval(value)
        return list_to_treenode(value)

    return value


def convert_from_type(value: Any, target_type: type) -> Any:
    if get_origin(target_type) is Union:
        args = get_args(target_type)
        for arg in args:
            if arg is not type(None):
                return convert_from_type(value, arg)

    if target_type is ListNode or isinstance(value, ListNode):
        if value is None:
            return []
        return listnode_to_list(value)

    if target_type is TreeNode or isinstance(value, TreeNode):
        if value is None:
            return []
        return treenode_to_list(value)

    return value
