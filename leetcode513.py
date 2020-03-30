# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        List=[]
        List.append(root)
        while List:
            root=List.pop(0)
            if root.right:
                List.append(root.right)
            if root.left:
                List.append(root.left)
        return root.val