class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            while nums[i]!=i+1 and nums[i]!=nums[nums[i]-1]:
                c=nums[i]
                nums[i]=nums[nums[i]-1]
                nums[c-1]=c
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return[nums[i],i+1]

