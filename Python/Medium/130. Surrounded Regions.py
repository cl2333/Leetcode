from collections import deque
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        
        for i in [0, len(board) - 1]:
            for j in range(len(board[0])):
                self.bfs(i, j, board)
        
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                self.bfs(i, j, board)
        

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                if board[i][j] == 'C':
                    board[i][j] = 'O'
                
        
    
    
    def bfs(self, i, j, board):
        queue = deque([(i,j)])
        
        while queue:
            i, j = queue.pop()
            if self.change(i, j, board):
                board[i][j] = "C"
                for (x, y) in directions:
                    new_i = i + x
                    new_j = j + y
                    queue.append((new_i, new_j))
            
            
    
    def change(self, i, j, board):
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O':
            return True
        else:
            return False