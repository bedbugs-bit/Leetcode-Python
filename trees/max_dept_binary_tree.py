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

