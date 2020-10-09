class Solution:
     def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i >0 and j >0:
                    grid[i][j] = min(grid[i-1][j]+grid[i][j], grid[i][j-1]+grid[i][j])
                elif i>0:
                    grid[i][j] = grid[i-1][j]+grid[i][j]
                elif j>0:
                    grid[i][j] = grid[i][j-1]+grid[i][j]
        return grid[-1][-1]
#     def minPathSum(self, grid: List[List[int]]) -> int:
        
#         result = []
#         def next(grid, i, j, curr):
#             if i == len(grid)-1 and j == len(grid[0])-1:
#                 result.append(curr)
            
#             elif i == len(grid)-1:
#                 next(grid,i,j+1,curr+grid[i][j+1])
#             elif j == len(grid[0])-1:
#                 next(grid,i+1,j,curr+grid[i+1][j])
#             else:
#                 next(grid,i+1,j,curr+grid[i+1][j])
#                 next(grid,i,j+1,curr+grid[i][j+1])
        
#         next(grid, 0, 0, grid[0][0])
#         return min(result)