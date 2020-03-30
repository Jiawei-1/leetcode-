# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        l=len(nums)//2
        root = TreeNode(nums[l])
        if len(nums)!=1 and len(nums)!=1:
            root.left=self.sortedArrayToBST(nums[:l])
            root.right=self.sortedArrayToBST(nums[l+1:])
        elif len(nums)==2:
            root.left=TreeNode(nums[0])
        return root
