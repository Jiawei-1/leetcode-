# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root ==None:
            return True
        return self.isSymmetric2(root.right,root.left)

    def isSymmetric2(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val:
            return self.isSymmetric2(l.right, r.left) and self.isSymmetric2(l.left, r.right)
        return False