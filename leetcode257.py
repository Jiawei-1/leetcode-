# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def DFS(root, cur):
            if not root.left and not root.right:
                ans.append(cur)
            if root.left:
                DFS(root.left, cur + '->' + str(root.left.val))
            if root.right:
                DFS(root.right, cur + '->' + str(root.right.val))


        if not root:
            return []
        cur = str(root.val)
        ans = []
        DFS(root, cur)
        return ans

