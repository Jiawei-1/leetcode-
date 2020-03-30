# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        Min=min(p.val,q.val)
        Max=max(p.val,q.val)
        if Max>=root.val and Min<=root.val:
            return root
        elif Max< root.val:
            return self.lowestCommonAncestor(root.left, p ,q)
        else:
            return self.lowestCommonAncestor(root.right, p ,q)