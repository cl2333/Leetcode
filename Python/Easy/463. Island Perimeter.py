class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans += 4
                    if i in range(n) and j-1 in range(m) and grid[i][j-1] == 1:
                        ans -= 1
                    if i in range(n) and j+1 in range(m) and grid[i][j+1] == 1:
                        ans -= 1
                    if j in range(m) and i-1 in range(n) and grid[i-1][j] == 1:
                        ans -= 1
                    if j in range(m) and i+1 in range(n) and grid[i+1][j] == 1:
                        ans -= 1

        return ans
        
    def islandPerimeter(self, grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))