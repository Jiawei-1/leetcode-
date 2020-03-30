# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.Min=0
        self.pre=None
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.midReturn(root)
        return self.Min
    
    def midReturn(self,root):
        if not root:
            return
        self.midReturn(root.left)
        if self.pre!=None:
            if self.Min==0:
                self.Min=-self.pre.val+root.val
            else:
                self.Min=min(self.Min,-self.pre.val+root.val)
        self.pre=root
        self.midReturn(root.right)
