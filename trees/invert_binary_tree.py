from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None # base case: empty tree

        # swap left and right children
        root.left, root.right = root.right, root.left

        # recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invert_tree_stack(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        stack = [root]
        while stack:
            node = stack.pop()  # Process the current node (Preorder: Root first)

            # Swap left and right children
            node.left, node.right = node.right, node.left

            # Push right child first, then left (so left is processed first in Preorder)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return root

    def bfs_invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()

            # Swap left and right children
            node.left, node.right = node.right, node.left

            # Add children to queue for processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root








