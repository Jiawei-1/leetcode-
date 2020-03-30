class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # if not prices:
        #     return 0
        # Min=prices[0]
        # ans=max(prices)-Min
        # for i,j in enumerate(prices):
        #     if j <Min:
        #         Min=j
        #         ans=max(ans,max(prices[i:])-Min)
        # if ans<0:
        #     return 0
        # else:
        #     return ans
        if not prices:
            return 0
        Min=prices[0]
        ans=0
        for i in prices:
            Min=min(Min,i)
            ans=max(ans,i-Min)
        return ans
# print(Solution().maxProfit([4,1]))