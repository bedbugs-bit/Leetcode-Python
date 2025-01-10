from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # prefix
        sums = defaultdict(int)
        sums[0] = 1

        def dfs(root, total):
            count = 0
            if root:
                total += root.val
                # find if there exists a prefix sum in this path total = prefix + target, if prefix exists then there is a targetSum in this path
                count = sums[total - targetSum]

                # Add value of this prefix sum
                sums[total] += 1

                count += dfs(root.left, total) + dfs(root.right, total)

                # remove this value of prefix sum as it has been explored
                sums[total] -= 1
            return count

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

            return count


