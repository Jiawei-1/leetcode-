class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        Str='!#'+'#'.join(s)+'#$'
        List=[0]*len(Str)
        right,center=0,0
        for i in range(1,len(Str)-1):
            if i < right:
                List[i]=min(right-i,List[2*center-i])
            while Str[i+List[i]+1]==Str[i-List[i]-1]:
                List[i]+=1
            if i+List[i]>right:
                center=i
                right=i+List[i]
        return sum((v+1)//2 for v in List)
# print(Solution().countSubstrings('aba'))