class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(1,len(triangle)):
            if i == 1:
                triangle[i] = [j + triangle[0][0] for j in triangle[i]]
                continue


            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j]+triangle[i-1][j]
                elif j == i:
                    triangle[i][j] = triangle[i][j]+triangle[i-1][j-1]
                else:
                    triangle[i][j] = min(triangle[i][j]+triangle[i-1][j-1], triangle[i][j]+triangle[i-1][j])
        
        return min(triangle[-1])
                    
            