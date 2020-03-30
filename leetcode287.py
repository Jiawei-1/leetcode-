class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        b=nums[0]
        a=nums[a]
        b=nums[nums[b]]
        while a!=b:
            a=nums[a]
            b=nums[nums[b]]
        a=nums[0]
        while a!=b:
            a=nums[a]
            b=nums[b]
        return a

