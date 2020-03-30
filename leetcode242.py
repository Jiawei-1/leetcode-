class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dic={}
        for char in s:
            if dic.get(char):
                dic[char]+=1
            else:
                dic[char]=1
        for char in t:
            if not dic.get(char):
                return False
            else:
                dic[char]-=1
        for key in dic:
            if dic[key]!=0:
                return False
        return True