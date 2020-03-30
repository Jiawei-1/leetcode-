class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dic={}
        Sum=0
        single=0
        for char in s:
            if dic.get(char)==None:
                dic[char]=1
            else:
                dic[char]+=1
        for char in dic:
            if dic[char]==1:
                single=1
            elif dic[char]%2==0:
                Sum+=dic[char]
            else:
                Sum+=dic[char]-1
                single=1
        Sum+=single
        return Sum
# print(Solution().longestPalindrome('ccc'))
