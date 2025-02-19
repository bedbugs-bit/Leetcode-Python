from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val = 0, left = None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]):

        # base case
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False


        return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

    def is_same_tree_bfs(self, p, q):
        q = deque([(p,q)])

        while q:
            node1, node2 = q.popleft()
            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            q.append((node1.left, node2.left))
            q.append((node1.right, node2.right))
        return True