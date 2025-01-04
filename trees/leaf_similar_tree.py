# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Helper function to find the leaf sequence of a tree
        def get_leaf_sequence(node):
            if not node:
                return []
            if not node.left and not node.right:  # It's a leaf node
                return [node.val]

            # Recursively collect leaf values from left and right subtrees
            left_leaves = get_leaf_sequence(node.left)
            right_leaves = get_leaf_sequence(node.right)

            return left_leaves + right_leaves

        # Get leaf sequences for both trees
        leaf_sequence1 = get_leaf_sequence(root1)
        leaf_sequence2 = get_leaf_sequence(root2)

        # Compare the two sequences
        return leaf_sequence1 == leaf_sequence2
