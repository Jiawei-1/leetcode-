class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return []
        for i in range(len(board)):
            self.DFS(board, i, 0)
            self.DFS(board, i, len(board[0]) - 1)
        for i in range(len(board[0])):
            self.DFS(board, 0, i)
            self.DFS(board, len(board) - 1, i)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board
    
    def DFS(self, board, i, j):
        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or board[i][j] != 'O':
            return
        board[i][j] = 'S'
        for a, b in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            self.DFS(board, i+a, j+b)