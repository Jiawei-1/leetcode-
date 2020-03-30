class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Max=0
        nums.append(0)
        last=-1
        for num in range(len(nums)):
            if nums[num]==0:
                if Max<num-last-1:
                    Max=num-last-1
                last=num
        return Max