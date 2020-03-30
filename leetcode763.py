class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        dicmax={}
        ans=[]
        for num,i in enumerate(S):
            dicmax[i]=num
        Max=0
        for nums,i in enumerate(S):
            Max=max(Max,dicmax[i])
            if nums==Max:
                ans.append(nums)
        for i in range(len(ans)-1,0,-1):
            ans[i]+=-ans[i-1]
        ans[0]+=1
        return ans