class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        def DFS(candidates, cur):
            if sum(cur) == n and len(cur) == k:
                ans.append(cur[:])
            for i, j in enumerate(candidates):
                if sum(cur) + j > n or len(cur) >= k:
                    break
                cur.append(j)
                DFS(candidates[i+1:], cur)
                cur.pop()
        DFS(candidates, [])
        return ans
                