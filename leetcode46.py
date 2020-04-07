class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = []
        def DFS(nums, cur):
            if not nums:
                ans.append(cur)
            for i, j in enumerate(nums):
                DFS(nums[:i]+nums[i+1:], cur + [j])
        DFS(nums, [])
        return ans