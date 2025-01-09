from typing import Optional, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            # Update the current path sum
            current_sum += node.val
            # Count paths with the required sum ending at this node
            path_count = prefix_sums.get(current_sum - targetSum, 0)

            # Update the prefix sums with the current sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

            # Recursively count paths in left and right subtrees
            path_count += dfs(node.left, current_sum)
            path_count += dfs(node.right, current_sum)

            # Backtrack: remove the current sum from the prefix sums
            prefix_sums[current_sum] -= 1
            if prefix_sums[current_sum] == 0:
                del prefix_sums[current_sum]

            return path_count

        # Initialize prefix sums with base case (sum = 0)
        prefix_sums: Dict[int, int] = {0: 1}
        return dfs(root, 0)
