class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return[-1,-1]
        i=0
        j=len(nums)-1
        while i<j:
            m=i+(j-i)//2
            if nums[m]>=target:
                j=m-1
            else:
                i=m+1
        if nums[j]!=target and (nums[j+1]!=target if j<len(nums)-1 else 1):
            return [-1,-1]
        if nums[j]!=target:
            l=j+1
        else:
            l=j
        i=0
        j=len(nums)-1
        while i<j:
            m=i+(j-i)//2
            if nums[m]>target:
                j=m-1
            else:
                i=m+1
        if nums[j]!=target:
            return [l,j-1]
        else:
            return [l,j]
# print(Solution().searchRange([0,0,0,8,9,79],8))