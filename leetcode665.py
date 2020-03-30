class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def check(nums):
            for i in range(1,len(nums)):
                if nums[i]<nums[i-1]:
                    return False
            return True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                return check(nums[:i]+(nums[i+1:] if i<len(nums)-1 else [])) or check(nums[:i-1]+(nums[i:] if i<len(nums)-1 else []))
        return True
# print(Solution().checkPossibility([3,3,4,1]))