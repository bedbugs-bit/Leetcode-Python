from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None # track the previous node
        self.min_diff = float('inf')

        def dfs_inorder(node):
            if not node:
                return

            # left subtree
            dfs_inorder(node.left)

            # process the current node
            if self.prev is not None:
                self.min_diff= min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            # right subtree
            dfs_inorder(node.right)

        dfs_inorder(root) # start the inorder traversal

        return self.min_diff




