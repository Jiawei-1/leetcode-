class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i=0
        j=len(s)-1
        words=['a','e','i','o','u','A','E','I','O','U']
        s=list(s)
        while i<j:
            if s[i] in words:
                if s[j] in words:
                    s[i],s[j]=s[j],s[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                if s[j] in words:
                    i+=1
                else:
                    i+=1
                    j-=1
        return ''.join(s)