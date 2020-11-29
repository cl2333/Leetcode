from collections import deque
directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        result = 0
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.is_valid(grid, visited, i, j):
                    self.find_island(i, j, grid, visited)
                    result += 1
        
        return result
    
    def find_island(self, i, j, grid, visited):
        queue = deque([(i,j)])
        
        while queue:
            i, j = queue.pop()
            for (x, y) in directions:
                new_i = x + i
                new_j = y + j
                
                if self.is_valid(grid, visited, new_i, new_j):
                    visited.add((new_i, new_j))
                    queue.append((new_i, new_j))
                
    
    def is_valid(self, grid, visited, i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in visited and grid[i][j] == "1":
            return True
        return False
        
        
        