class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n, 0, -1)]
        
        for i in range(n):
            dp[i][i] = 1
            
        

        for i in range(1, n):
            for j in range(i):
                if s[i] == s[j] and (dp[j + 1][i - 1] == 1 or j == i - 1):
                    dp[j][i] = 1
        

        res = 0
        for i in range(n):
            res += sum(dp[i])
        
        return res

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1) < 3 or dp[i+1][j-1])
                res += dp[i][j]
        return res      
