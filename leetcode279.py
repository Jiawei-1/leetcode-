import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack=[n]
        stack2=[]
        num=1
        while stack!=[]:
            while stack!=[]:
                cur=stack.pop(0)
                Max=int(cur**0.5)
                if Max*Max==cur:
                    return num
                for i in range(Max,0,-1):
                    stack2.append(cur-i*i)
            num+=1
            stack=stack2
            stack2=[]
# print(Solution().numSquares(7168))