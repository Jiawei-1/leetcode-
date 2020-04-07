class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 0:
            return []
        empty = [(i, j) for i in range(n) for j in range(n)]
        ans = []
        def backtrace(j, cur, empty):
            if len(cur) == n:
                ans.append(cur)
                return
            if empty == []:
                return False
            for i in range(n):
                if (j, i) in empty:
                    word = '.' * i + 'Q' + '.' * (n - 1 - i)
                    cur.append(word)
                    empty2 = empty[:]
                    for num in range(len(empty2)-1, -1, -1):
                        (a, b) = empty2[num]
                        if a == j or b == i or a + b == j + i or a - b == j - i:
                            empty2.pop(num)
                    backtrace(j + 1, cur[:], empty2)
                    cur.pop()
        backtrace(0, [], empty)
        return ans
# print(Solution().solveNQueens(15))
            