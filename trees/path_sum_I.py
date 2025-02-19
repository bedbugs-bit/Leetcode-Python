# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSumDfsIterative(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == targetSum:
                return True

            if curr.right:
                stack.append((curr.right, val + curr.right.val))
            if curr.left:
                stack.append((curr.left, val + curr.left.val))

        return False

    def has_path_sum_dfs_recursive(self, root, target_sum):
        def dfs(node, curr_sum):

            # base case: of tree is empty
            if not node:
                return False

            curr_sum += node.val

            # If it's a leaf node, check if sum matches targetSum
            if not node.left and not node.right:
                return curr_sum == target_sum

            # Recursive DFS call for left and right subtrees
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

        return dfs(root, 0)
