# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum=0
        if root == None:
            return sum
        if root.left and root.left.left==None and root.left.right==None:
            sum+=root.left.val
        sum=sum+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        return sum
