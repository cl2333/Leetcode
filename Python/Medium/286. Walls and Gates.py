from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def bfs(i, j):
            queue = deque([(i,j)])
            while queue:
                x, y = queue.popleft()
                for (i,j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_x, new_y = x + i, y + j
                    if 0 <= new_x < len(rooms) and 0 <= new_y < len(rooms[0]) and rooms[new_x][new_y] != -1 and rooms[x][y] + 1 <  rooms[new_x][new_y]:
                        rooms[new_x][new_y] = rooms[x][y] + 1
                        queue.append((new_x,new_y))
    
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == -1 or rooms[i][j] == 2147483647:
                    continue
                bfs(i, j)
    
    
        