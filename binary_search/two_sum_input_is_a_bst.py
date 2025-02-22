# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        q = deque([root])
        hash_set = set()

        while q:
            node = q.popleft()

            if (k - node.val) in hash_set:
                return True
            else:
                hash_set.add(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return False

