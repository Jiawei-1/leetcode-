class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []
        ans = []
        def DFS(s, cur):
            if not s:
                ans.append(cur[:])
            for i in range(1, len(s)+1):
                if self.isLoop(s[:i]):
                    cur.append(s[:i])
                    DFS(s[i:], cur)
                    cur.pop()
        DFS(s, [])
        return ans
    
    def isLoop(self, s):
        if not s:
            return False
        j = len(s) - 1
        i = 0
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True