class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        ans=[]
        for i,j in enumerate(input):
            if j in ['+','-','*']:
                left=self.diffWaysToCompute(input[:i])
                right=self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right: 
                        if j=='+':
                            ans.append(l+r)
                        elif j=='-':
                            ans.append(l-r)
                        elif j=='*':
                            ans.append(l*r)
        return ans