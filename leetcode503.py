class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        Max = 0
        l=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)):
            if nums[i] >= nums[Max]:
                Max=i
        for i in range (Max, Max-len(nums),-1):
            while stack and nums[i]>= nums[stack[-1]]:
                stack.pop()
            if stack:
                l[i]=nums[stack[-1]]
            stack.append(i)
        return l


