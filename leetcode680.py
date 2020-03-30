class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else: 
                return self.search(s[i+1:j+1]) or self.search(s[i:j])
        return True
    def search(self,s):
        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            else: 
                return False
        return True
# print(Solution().validPalindrome('abc'))