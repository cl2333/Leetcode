class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        result = 0
        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = i
            else:
                if start <= mapping[s[i]]:
                    start = mapping[s[i]] + 1
                mapping[s[i]] = i
                
            result = max(result, i - start + 1)
        
        return result
            
            
            