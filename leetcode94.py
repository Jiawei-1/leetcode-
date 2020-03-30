# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack=[root,]
        Output=[]
        while stack:
            while root:
                root=root.left
                if root:
                    stack.append(root)
            root = stack.pop()
            Output.append(root.val)
            root=root.right
            if root:
                stack.append(root)
        return Output