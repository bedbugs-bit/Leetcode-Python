from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth_recursive_dfs(self, root:Optional[TreeNode]) -> int:

        if not root:
            return 0

        return 1 + max(self.max_depth_recursive_dfs(root.left), self.max_depth_recursive_dfs(root.right))

    def max_depth_bfs(self, root: Optional[TreeNode]) ->int:
        if not root:
            return 0

        level = 0

        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            level += 1

        return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0  # No tree, depth is 0

        q = deque([(root, 1)])  # Queue stores (node, current depth)

        while q:
            node, level = q.popleft()

            # Add left and right children to queue if they exist
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return level




