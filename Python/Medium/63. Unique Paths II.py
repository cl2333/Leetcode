class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        result = [[0] * len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    result[i][j] = 0
                else:
                    if i==0 and j==0:
                        result[i][j] = 1
                    elif i==0:
                        result[i][j] = result[i][j-1]
                    elif j==0:
                        result[i][j] = result[i-1][j]
                    else:
                        result[i][j] = result[i-1][j] + result[i][j-1]
        
        return result[-1][-1]