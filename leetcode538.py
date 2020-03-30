# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        cur=root 
        stack=[]
        sum=0
        while stack or root:
            while root:
                stack.append(root)
                root=root.right
            root=stack.pop()
            sum+=root.val
            root.val=sum
            root=root.left
        return cur
