class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack=[]
        l=[0]*len(T)
        for i in range(len(T)-1, -1, -1):
            while stack and T[i]>= T[stack[-1]]:
                stack.pop()
            if stack:
                l[i]=stack[-1]-i
            stack.append(i)
        return l
