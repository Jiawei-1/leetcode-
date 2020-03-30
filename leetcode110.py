# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedHelper(root)[0]
    
    def isBalancedHelper(self,root):
        if not root:
            return True,0
        
        LeftisBalance, Hleft= self.isBalancedHelper(root.left)
        if not LeftisBalance:
            return False,0
        RightisBalance, Hright= self.isBalancedHelper(root.right)
        if not RightisBalance:
            return False, 0
        return abs(Hleft-Hright)<2, 1+max(Hright,Hleft)