class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        ans = []
        curr = []
        def DFS(i, n, cur):
            if len(cur) == k:
                ans.append(cur[:])
            if i == n+1:
                return
            for j in range(i, n+1):
                cur.append(j)
                DFS(j+1, n, cur)
                cur.pop()
        DFS(1, n, curr)
        return ans