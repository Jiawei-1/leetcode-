class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if i > 0 and candidates[i-1] == j:
                    continue
                cur.append(j)
                DFS(candidates[i+1:], cur)
                cur.pop()
        DFS(candidates, [])
        return ans
                