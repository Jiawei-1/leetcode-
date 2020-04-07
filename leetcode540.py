class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        h=len(nums)-1
        while l<h:
            m=l+(h-l)//2
            if m % 2 == 0:
                if nums[m]==nums[m+1]:
                    l+=1
                else:
                    h-=1
            else:
                if nums[m]==nums[m-1]:
                    l+=1
                else:
                    h-=1
        return nums[l]
# print(Solution().singleNonDuplicate([0,1,1]))