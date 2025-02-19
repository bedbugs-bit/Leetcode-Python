# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # No tree, depth is 0

        q = deque([(root, 1)])  # Queue stores (node, current depth)

        while q:
            node, level = q.popleft()

            # If we reach a leaf node, return its depth
            if not node.left and not node.right:
                return level

            # Add left and right children to queue if they exist
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return -1  # This case will never be reached


