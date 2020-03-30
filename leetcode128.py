class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set(nums)
        Max=0
        for num in nums_set:
            if num-1 not in nums_set:
                cur_num=num
                cur_length=1
                while cur_num+1 in nums_set:
                    cur_length+=1
                    cur_num+=1
                Max=max(Max,cur_length)
        return Max