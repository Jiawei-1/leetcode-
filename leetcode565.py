class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[0]*len(nums)
        Max=0
        for i in range(len(nums)):
            if l[i]==1:
                continue
            count=1
            l[i]=1
            s=nums[i]
            while s!=i:
                l[s]=1
                s=nums[s]
                count+=1
            Max=max(Max,count)
        return Max
# print(Solution().arrayNesting([3,1,4,0,2]))

            
