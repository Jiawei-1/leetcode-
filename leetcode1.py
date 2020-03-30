class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]:
            return
        dic={}
        for i, num in enumerate(nums):
            if dic.get(target-num)==None:
                dic[num]=i
            else:
                return dic[target-num],i