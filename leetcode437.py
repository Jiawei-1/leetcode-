# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSumRoot(self,root,sum):
        if not root:
            return 0
        ans=0
        if root.val==sum:
            ans+=1
        ans=ans+self.pathSumRoot(root.right,sum-root.val)+self.pathSumRoot(root.left, sum-root.val)
        return ans
        
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumRoot(root,sum)+self.pathSum(root.right,sum)+self.pathSum(root.left, sum)

