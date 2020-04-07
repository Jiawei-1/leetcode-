class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = [[]]
        nums.sort()
        def DFS(nums, l, cur):
            if len(cur) == l:
                ans.append(cur[:])
            for i,j in enumerate(nums):
                if i > 0 and nums[i-1] == j:
                    continue
                cur.append(j)
                DFS(nums[i+1:], l, cur)
                cur.pop()
        for i in range(len(nums)):
            DFS(nums, i+1, [])
        return ans