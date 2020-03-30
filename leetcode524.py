class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        Max=''
        for S in d:
            i=0
            j=0
            while i<len(s) and j<len(S):
                if s[i]==S[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if j ==len(S) and len(S)>len(Max):
                Max=S
            elif j ==len(S) and len(S)==len(Max):
                Max=min(Max,S)
        return Max
# print(Solution().findLongestWord("abpcplea",["ale","apple","monkey","plea"]))