class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dic={}
        Max=0
        for i in nums:
            if dic.get(i)==None:
                dic[i]=1
            else:
                dic[i]+=1
        for key in dic:
            if dic.get(key+1) !=None:
                Max=max(Max, dic[key]+dic[key+1])
        return Max