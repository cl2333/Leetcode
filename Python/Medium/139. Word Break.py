class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True                    
        
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        max_len = max([len(word) for word in wordDict]) if wordDict else 0
        for i in range(1, len(s) + 1):
            for l in range(1, max_len + 1):
                
                if i < l:
                    break
                
                if not dp[i - l]:
                    continue
                
                if s[i - l: i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]