class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def DFS(grid, i, j, count):
            for a, b in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                if i+a >=0 and i+a < len(grid) and j+b >= 0 and j+b < len(grid[0]):
                    if grid[i+a][j+b] == 1:
                        grid[i+a][j+b] = 2
                        count += 1
                        count = DFS(grid, i+a, j+b, count)
            return count

        if not grid:
            return 0
        Max = 0
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    count = 1
                    grid[i][j] =2
                    count = DFS(grid, i, j, count)
                    Max = max(Max, count)
        return Max
