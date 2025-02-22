# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        curr = root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = new_node
                    break
            else:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = new_node
                    break

        return root

    def dfs_recursive(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        if val < root.val:
            root.left = self.dfs_recursive(root.left,val)

        else:
            root.right = self.dfs_recursive(root.right, val)

        return root









