class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dic={}
        dic2={}
        for i in range(len(s)):
            if dic.get(s[i])!=None:
                if dic[s[i]]!=ord(s[i])-ord(t[i]):
                    return False
            else:
                dic[s[i]]=ord(s[i])-ord(t[i])

            if dic2.get(t[i])!=None:
                if dic2[t[i]]!=ord(s[i])-ord(t[i]):
                    return False
            else:
                dic2[t[i]]=ord(s[i])-ord(t[i])
        return True
# print(Solution().isIsomorphic('ab','aa'))