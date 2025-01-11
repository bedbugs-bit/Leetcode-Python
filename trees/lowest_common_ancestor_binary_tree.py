from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        def dfs(node, p, q):
            # Base case: If the current node is None or matches p or q
            if not node or node == p or node == q:
                return node

            # Recursively search left and right subtrees
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            # If both sides return non-None, the current node is the LCA
            if left and right:
                return node

            # Otherwise, return the non-None value (or None if both are None)
            return left if left else right

        # Start the DFS from the root
        return dfs(root, p, q)

    def lowestCommonAncestor_2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        dfs, bottom up
        '''

        '''
        Time: O(n), traverse through each node once operate O(1) in each node
        Space: O(height):
            heap: O(1)
            stack: O(height) where height is the tree height
        '''

        # base case
        if not root or root == p or root == q:
            return root

        # recursion 3 steps
        # 1. what do I want from my child? check right or left have LCA
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)

        # 2. what do I do at current level?
        # 3. what to return?
        # case 1: if current node's left and right both find LCA, return node it self since it will be the LCA
        # case 3: if current node's left find one of the target, and right does not, return left to tell your parent that one of the target has been found in left
        # case 4: if current node's right find one of the target, and left does not, return right to tell your parent that one of the target has been found in right
        # case 5: if both left and right child find nothing, return None

        if leftLCA and rightLCA:
            return root
        elif leftLCA and not rightLCA:
            return leftLCA
        elif rightLCA and not leftLCA:
            return rightLCA
        else:
            return None
