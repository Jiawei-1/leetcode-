class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l=0
        h=len(letters)-1
        while l<=h:
            m=l+(h-l)//2
            if letters[m]==target:
                return letters[m+1]
            elif letters[m]<target:
                h=m-1
            else:
                l=m+1
        return letters[l] if letters[l]>target else letters[0]