class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {'2' : 'abc', '3' : 'def', '4' : 'ghi',
                '5' : 'jkl', '6' : 'mno', '7' : 'pqrs', 
                '8' : 'tuv', '9' : 'wxyz'}
        ans = []
        def DFS(combination, digits):
            if not digits:
                ans.append(combination)
            else:
                for letter in dic[digits[0]]:
                    DFS(combination + letter, digits[1:])
        DFS('', digits)
        return ans