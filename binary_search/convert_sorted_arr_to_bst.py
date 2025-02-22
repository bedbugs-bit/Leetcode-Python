# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:  # Base case: Empty array
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        # recursively construct left and right subtrees
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1: ])

        return root

    def bfs_solution(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        queue = deque([(root, 0, len(nums) - 1)])

        while queue:
            node, left, right = queue.popleft()
            mid = (left + right) // 2

            if left < mid:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                queue.append((node.left, left, mid - 1))

            if mid < right:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                queue.append((node.right, mid + 1, right))

        return root