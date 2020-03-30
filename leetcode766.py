class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if i!=0 and j!=0 and matrix[i-1][j-1]!=val:
                    return False
        return True
# print(Solution().isToeplitzMatrix([[1,2],[2,2]]))