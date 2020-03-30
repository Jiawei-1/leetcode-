# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        stack=[root,]
        root=root.left
        while stack:
            while root:
                stack.append(root)
                root=root.left
            cur=stack.pop()
            k-=1
            if k ==0:
                return cur.val
            root=cur.right
            if root:
                stack.append(root)
                root=root.left
        
        