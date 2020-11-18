class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s:
            return 0
        
        n = len(s)
        is_Palindrome = [[0] * n for _ in range(n)]
        
        for i in range(n):
            is_Palindrome[i][i] = 1
        
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length -1 
                if s[i] == s[j]:
                    is_Palindrome[i][j] = 2 + is_Palindrome[i+1][j-1]
                else:
                    is_Palindrome[i][j] = max(is_Palindrome[i+1][j], is_Palindrome[i][j-1])
        
        return is_Palindrome[0][n-1] 