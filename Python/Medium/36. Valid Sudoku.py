class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        repeat = []
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    cur = board[i][j]
                    if (i,cur) in repeat or (cur,j) in repeat or (i//3,j//3,cur) in repeat:
                        return False
                    repeat.append((i,cur))
                    repeat.append((cur,j))
                    repeat.append((i//3,j//3,cur))
        return True
                
        