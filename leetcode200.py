class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def DFS(grid, i, j):
            for a, b in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if i+a >=0 and i+a < len(grid) and j+b >= 0 and j+b < len(grid[0]):
                    if grid[i+a][j+b] == '1':
                        grid[i+a][j+b] = '0'
                        DFS(grid, i+a, j+b)
            return

        if not grid:
            return 0
        ans = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    ans += 1 
                    grid[i][j] = '0'
                    DFS(grid, i, j)
        return ans
