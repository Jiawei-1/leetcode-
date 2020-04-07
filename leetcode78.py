class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = [[]]
        def DFS(nums, l, cur):
            if len(cur) == l:
                ans.append(cur[:])
            for i,j in enumerate(nums):
                cur.append(j)
                DFS(nums[i+1:], l, cur)
                cur.pop()
        for i in range(len(nums)):
            DFS(nums, i+1, [])
        return ans