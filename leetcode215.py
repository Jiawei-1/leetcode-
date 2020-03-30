import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # left=0
        # right=len(nums)-1
        # k=len(nums)-k

        # def quicksort(nums,left,right):
        #     key=nums[left]
        #     while left<right:
        #         while left<right and nums[right]>=key:
        #             right-=1
        #         if left<right:
        #             nums[left]=nums[right]
        #         while left<right and nums[left]<=key:
        #             left+=1
        #         if left<right:
        #             nums[right]=nums[left]
        #     nums[left]=key
        #     return left

        # cur=quicksort(nums,left,right)
        # while cur!=k:    
        #     if cur > k:
        #         right=cur-1
        #         cur=quicksort(nums,left,right)
        #     else:
        #         left=cur+1
        #         cur=quicksort(nums,left,right)

        # return nums[k]
        return heapq.nlargest(k,nums)