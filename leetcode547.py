class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        List = [0] * N
        ans = 0
        for i in range(N):
            if List[i] == 0:
                ans += 1
                List[i] = 1
                self.DFS(M, i, List)
        return ans
    def DFS(self, M, i, List):
        for j in range(len(M)):
            if M[i][j] == 1:
                if List[j] == 0:
                    List[j] = 1
                    self.DFS(M, j, List)
                