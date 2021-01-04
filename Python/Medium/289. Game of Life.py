class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                neighbors = self.count(board, i, j)
                if board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                    board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0
    
    
    def count(self, board, i, j):
        result = 0
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
            x, y = i + di, j + dj
            if 0 <= x < len(board) and 0 <= y < len(board[0]):
                result += board[x][y] % 2
            
        return result