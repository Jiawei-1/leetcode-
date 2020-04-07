class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        def isValid(board, row, col, a):
            for i in range(9):
                if board[i][col] == a:
                    return False
                if board[row][i] == a:
                    return False
                r = (row // 3) * 3 + i // 3
                c = (col // 3) * 3 + i % 3 
                if board[r][c] == a:
                    return False
            return True
        def backtrace(board, row, col):
            if col == 9:
                return backtrace(board, row + 1, 0) 
            if row == 9:
                return True
            if board[row][col] != '.':
                return backtrace(board, row, col + 1)
            for c in range(1, 10):
                if not isValid(board, row, col, str(c)):
                    continue
                board[row][col] = str(c)
                if backtrace(board, row, col + 1):
                    return True
                board[row][col] = '.'
            return False
        if not board:
            return 
        backtrace(board, 0 ,0)
        return board