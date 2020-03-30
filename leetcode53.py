class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        Min=0
        Max=nums[0]
        Sum=0
        for i in nums:
            Sum+=i
            Max=max(Max,Sum-Min)
            Min=min(Min,Sum)
        return Max