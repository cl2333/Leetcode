class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        result = []
        nr, nc = len(matrix), len(matrix[0])
        seen = [[False] * nc for _ in matrix]
        
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        r = c = i = 0
        
        for _ in range(nr*nc):
            result.append(matrix[r][c])
            seen[r][c] = True
            
            r_next = r + dr[i]
            c_next = c + dc[i]
            
            if 0 <= r_next < nr and 0 <= c_next < nc and not seen[r_next][c_next]:
                r, c = r_next, c_next
            else:
                i = (i+1)%4
                r, c = r + dr[i], c + dc[i]
            
        return result
            
            
            
            