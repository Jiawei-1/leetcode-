class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        ans = []
        candidates = sorted(candidates)
        def DFS(candidates, cur):
            if sum(cur) == target:
                ans.append(cur[:])
            for i, j in enumerate(candidates):
                if sum(cur) + j > target:
                    break
                cur.append(j)
                DFS(candidates[i:], cur)
                cur.pop()
        DFS(candidates, [])
        return ans
                