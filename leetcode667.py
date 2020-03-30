class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        l=[]
        for i in range(n-k):
            l.append(i+1)
        for i in range(k,0,-1):
            if i % 2 == k % 2:
                l.append(l[-1]+i)
            else:
                l.append(l[-1]-i)
        return l