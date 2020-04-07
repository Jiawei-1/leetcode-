class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre1 = 1
        pre2 = 2
        for i in range(n - 2):
            cur = pre1 + pre2
            pre1 = pre2
            pre2 = cur
        return cur