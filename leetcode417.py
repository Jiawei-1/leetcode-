class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        h = len(matrix)
        w = len(matrix[0])
        ans =[]
        matrixP = [[0 for _ in range(w) ] for _ in range(h)]
        matrixA = [[0 for _ in range(w) ] for _ in range(h)]
        for i in range(h):
            self.DFS(matrix, i, 0, matrixP)
            self.DFS(matrix, i, w-1, matrixA)
        for i in range(w):
            self.DFS(matrix, 0, i, matrixP)
            self.DFS(matrix, h-1, i, matrixA)
        for i in range(h):
            for j in range(w):
                if matrixP[i][j] == 1 and matrixA[i][j]==1:
                    ans.append([i,j])
        return ans

    def DFS(self, matrix, i, j, m):
        if m[i][j] == 1:
            return
        m[i][j] = 1
        for a, b in ([0, 1], [1, 0], [-1, 0], [0, -1]):
            if i+a >= 0 and i+a <len(matrix) and j+b >=0 and j+b <len(matrix[0]) and matrix[i][j] <= matrix[i+a][j+b]:
                self.DFS(matrix, i+a, j+b, m)
