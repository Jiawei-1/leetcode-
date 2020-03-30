class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        side0=0
        side2=len(nums)-1
        cur=0
        while cur<=side2:
            if nums[cur]==0:
                nums[cur],nums[side0]=nums[side0],nums[cur]
                cur+=1
                side0+=1
            elif nums[cur]==1:
                cur+=1
            elif nums[cur]==2:
                nums[cur],nums[side2]=nums[side2],nums[cur]
                side2-=1
        return nums
print(Solution().sortColors([1,0,2]))