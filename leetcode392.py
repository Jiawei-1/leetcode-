class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        idx=-1
        for i in s:
            idx=t.find(i,idx+1)
            if idx==-1:
                return False
        return True