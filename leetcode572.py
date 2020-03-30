# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def istree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s==None and t==None:
            return True
        if not (s and t):
            return False
        if s.val==t.val:
            return self.istree(s.left,t.left) and self.istree(s.right,t.right)
        return False
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s==None and t!=None:
            return False
        return self.istree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
