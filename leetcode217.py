class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if not nums:
        #     return False
        # dic={}
        # for i in nums:
        #     if dic.get(i)==None:
        #         dic[i]=1
        #     else:
        #         return True
        # return False
        if not nums or len(nums)==1:
            return False
        list.sort(nums)
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        else:return False