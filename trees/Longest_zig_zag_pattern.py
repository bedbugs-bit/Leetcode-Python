# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def __init__(self):
        self.max_zigzag = 0

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        

        
        def dfs(node, is_left, length):
            if not node:
                return 0
            
            self.max_zigzag = max(self.max_zigzag, length)

            if is_left:
                dfs(node.left, False, length + 1)
                dfs(node.right, True, 1)

            else:
                dfs(node.right, True, length + 1)
                dfs(node.left, False, 1)

        dfs(root, True, 0)
        dfs(root, False, 0)

        return self.max_zigzag


    def longestZigZag2(self, root: Optional[TreeNode]) -> int:
        def helper(root, length, left):
            if not root:
                return length
            length += 1
            if left:
                return max(helper(root.right, length, False), helper(root.left, 0, True))
            return max(helper(root.left, length, True), helper(root.right, 0, False))
        return helper(root, -1, False)

    def longestZigZag3(self, root: Optional[TreeNode]) -> int:
        ans = 0
        # Meaning of l,r:
        # l means the longest zigzag path with node as end point, moreover,
        # node is the left child of its parent.
        # Similarly, define r.
        def dfs(node:TreeNode,l:int,r:int):
            nonlocal ans
            ans = max(ans,l)
            ans = max(ans,r)
            if node.left:
                dfs(node.left,r+1,0)
            if node.right:
                dfs(node.right,0,l+1)
        dfs(root,0,0)
        return ans
            