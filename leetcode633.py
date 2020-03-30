import numpy
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a=0
        b=c
        while a<b:
            b=numpy.sqrt(c-a*a)
            if b==int(b):
                return True
            a+=1
        return False