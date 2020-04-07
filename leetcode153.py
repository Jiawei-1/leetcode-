class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=len(nums)-1
        while i<j:
            m=i+(j-i)//2
            if nums[m]>nums[j]:
                i=m+1
            else:
                if nums[m]<nums[m-1]:
                    return nums[m]
                else:
                    j=m-1
        return nums[i]
# print(Solution().findMin([7,8,0,1,2,3,4,5,6]))