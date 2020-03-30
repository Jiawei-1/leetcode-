# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        if root.left and root.left.val>root.val:
            left=root.left.val
        else:
            left=self.findSecondMinimumValue(root.left)
        if root.right and root.right.val>root.val:
            right=root.right.val
        else:
            right=self.findSecondMinimumValue(root.right)
        if left>0 and right>0:
            return min(left,right)
        else:
            return max(left,right)
        