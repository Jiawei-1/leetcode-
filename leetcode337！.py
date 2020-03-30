# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob2(root):
            if not root:
                return 0,0
            left, leftno = rob2(root.left)
            right,rightno = rob2(root.right)
            return max(leftno+rightno+root.val, right+left), right+left
        return rob2(root)[0]


# 太牛逼了 我人傻了