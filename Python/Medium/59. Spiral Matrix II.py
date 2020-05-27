class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0]*n for i in range(n)]
        
        seen = [[False]*n for i in range(n)]
        
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        
        c=r=di=0
        
        for i in range(n*n):
            result[r][c] = i+1
            seen[r][c] = True
            
            r_next = r + dr[di]
            c_next = c + dc[di]
            
            if 0 <= c_next < n and 0 <= r_next < n and not seen[r_next][c_next]:
                r = r_next
                c = c_next
            else:
                di = (di+1)%4
                r = r + dr[di]
                c = c + dc[di]
        
        return result