class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def search(self, root, val: int):
        if not root:
            return None

        if root.val == val:
            return root

        elif root.val > val:
            return self.search(root.left, val)
        else:
            return  self.search(root.right, val)

