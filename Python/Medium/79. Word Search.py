class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def find(i, j, cur, board, word, index):
            if index == len(word) :
                return True
            
            if index >= len(word) or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '#'
            
            res = find(i+1, j, cur+ board[i][j], board, word, index+1) or find(i-1, j, cur+ board[i][j], board, word, index+1) or find(i, j+1, cur+ board[i][j], board, word, index+1) or find(i, j-1, cur+ board[i][j], board, word, index+1)
            
            board[i][j] = tmp
            
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if find(i,j, "", board, word, 0):
                    return True
            
            
            
            
            