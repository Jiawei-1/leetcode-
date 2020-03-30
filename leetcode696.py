class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sum=0
        # for i in range(len(s)-1):
        #     if int(s[i])+int(s[i+1])==1:
        #         Sum+=1
        #         j=1
        #         while i-j>=0 and i+j+1<len(s) and int(s[i-j])+int(s[i+j+1])==1 and s[i-j]==s[i]:
        #             Sum+=1
        #             j+=1
        # return Sum
        if not s:
            return 0
        ans,pre,cur=0,0,1
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                ans+=min(pre,cur)
                pre,cur=cur,1
            else:
                cur+=1
        return ans+min(pre,cur)