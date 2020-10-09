class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = 1
        
        for i in range(m+n-2,m-1,-1):
            result *= i
        
        for i in range(1,n):
            result /= i
        
        return int(result)