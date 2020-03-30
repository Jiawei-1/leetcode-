class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        Min=matrix[0][0]
        Max=matrix[n-1][n-1]
        while Min<=Max:
            count=0
            mid=(Min+Max)//2
            for i in range(n):
                for j in range(n):
                    if matrix[i][j]<=mid:
                        count+=1
                    else: 
                        break
            if count>=k:
                Max=mid-1
            else:
                Min=mid+1
        return Min
