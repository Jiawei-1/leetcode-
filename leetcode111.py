# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root ==None:
            return 0
        l=self.minDepth(root.left)
        r=self.minDepth(root.right)
        if r==0 or l==0:
            return max(r,l)+1
        return min(l,r)+1