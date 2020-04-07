class Solution(object):
    def permuteUnique(self, nums):
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
                if i >= 1 and nums[i-1] == j:
                    continue
                DFS(nums[:i] + nums[i+1:], cur + [j])
        nums = sorted(nums)
        DFS(nums, [])
        return ans