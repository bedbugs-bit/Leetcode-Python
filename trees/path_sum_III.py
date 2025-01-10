from collections import defaultdict
from typing import Optional, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        # Initialize prefix sums with base case (sum = 0)
        # We have seen a sum of zero once.
        prefix_sums: Dict[int, int] = {0: 1}

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


        return dfs(root, 0)


    def pathSum2(self, root, targetSum):
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            count = prefix_sum[curr_sum - targetSum]

            prefix_sum[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefix_sum[curr_sum] -= 1

            # Space complexity of O(n) and time complexity of O(n)
            return count




