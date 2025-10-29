# 236
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)

    def find(self, root, p, q):
        if root is None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)
        if left and right:
            return root
        return left if left else right  