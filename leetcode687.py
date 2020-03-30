# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def longestUnivaluePathRoot(root):
            if not root:
                return 0
            lef=longestUnivaluePathRoot(root.left)
            rig=longestUnivaluePathRoot(root.right)
            lef_now, rig_now=0,0
            if root.left and root.left.val == root.val:
                lef_now=lef+1
            if root.right and root.right.val==root.val:
                rig_now=rig+1
            self.ans=max(self.ans,rig_now+lef_now)
            return max(rig_now, lef_now)
        longestUnivaluePathRoot(root)
        return self.ans
