class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        N = len(grid)
        if grid[0][0] ==1 or grid[N-1][N-1]==1:
            return -1
        if grid ==[[0]]:
            return 1
        stack=[[0,0]]
        stack2=[]
        num=1
        while stack!=[]:
            num+=1
            for i,j in stack:
                grid[i][j]=2
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if x==N-1 and y==N-1:
                            return num
                        if x>=0 and y>=0 and x<N and y<N:
                            if grid[x][y] ==0:
                                stack2.append([x,y])
                                grid[x][y]=2
            stack=stack2
            stack2=[]
        return -1

