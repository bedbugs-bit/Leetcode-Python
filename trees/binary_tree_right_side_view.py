from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def right_side(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            size = len(q)
            right_side_view = None

            for _ in range(size):
                node = q.popleft()
                if node:
                    right_side_view = node
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            res.append(right_side_view.val)


