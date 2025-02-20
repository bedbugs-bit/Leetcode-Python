# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameter_of_binary_tree_iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)] # node, visited flag
        node_to_height = {}
        max_diameter = 0

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                # calculate the height
                left_height = node_to_height.get(node.left, 0)
                right_height = node_to_height.get(node.right, 0)

                # update max_diameter
                max_diameter = max(max_diameter, left_height + right_height)

                # store height
                node_to_height[node] = 1 + max(left_height, right_height)

            else:
                # Preorder step: Push nodes with visited flag
                stack.append((node, True))  # Process after children
                stack.append((node.right, False))
                stack.append((node.left, False))

        return max_diameter

    def diameter_of_binary_tree(self, root: [TreeNode]):
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return  0


            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # update teh same variable across all recursive calls
            self.max_diameter = max(self.max_diameter, left_height + right_height)

            return  1 + max(left_height, right_height)

        dfs(root)
        return self.max_diameter




