class Solution:
    def __init__(self):
        self.dp = {}
    
    def numTrees(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        if n == 0 or n == 1:
            return 1
        count = 0
        for i in range(1, n+1):
            count += self.numTrees(i-1) * self.numTrees(n-i)
        
        self.dp[n] = count
        return count