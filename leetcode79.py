class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        def DFS(board, word, i, j):
            if not word:
                return True
            if len(word) == 1 and board[i][j] == word[0]:
                return True
            if board[i][j] != word[0]:
                return  False
            cur = board[i][j]
            board[i][j] = ''
            for a, b in ([0, 1], [1, 0], [-1, 0], [0, -1]):
                if i+a >= 0 and i+a <len(board) and j+b >=0 and j+b < len(board[0]):# and board[i+a][j+b] == word[0]
                    if DFS(board, word[1:], i+a, j+b):
                        return True
            board[i][j] = cur

        for i in range(len(board)):
            for j in range(len(board[0])):
                if DFS(board, word, i, j):
                    return True
        return False
# print(Solution().exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],"aaaaaaaaaaaaa"))