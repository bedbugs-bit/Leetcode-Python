from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        def dfs(node, p, q):
            # Base case: If the current node is None or matches p or q
            if node == p or node == q:
                return node # Base case

            if not node:
                return None # Base case

            # Recursively search left and right subtrees
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            # If both sides return non-None, the current node is the LCA
            if left and right:
                return node

            # Otherwise, return the non-None value (or None if both are None)
            # return left if left else right
            if left:
                return left

            if right:
                return right

            if not left and not right:
                return None

        # Start the DFS from the root
        return dfs(root, p, q)




