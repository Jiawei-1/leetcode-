class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, l={},{},{}
        if not nums:
            return 0
        for i,s in enumerate(nums):
            if s not in left:
                left[s]=i
                l[s]=1
            else:
                right[s]=i
                l[s]+=1
        if not right:
            return 1

        Max=max(l.values())
        Min=len(nums)
        for s in l:
            if l[s]==Max:
                Min=min(Min, right[s]-left[s]+1)
        return Min

# print(Solution().findShortestSubArray([1,2,2,3,2,1,1]))