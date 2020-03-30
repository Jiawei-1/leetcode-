class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        if x < 0 or x %10==0:
            return False
        val=0
        while x>val:
            val=val*10+x%10
            x=x//10
        return x==val or x==val//10
    