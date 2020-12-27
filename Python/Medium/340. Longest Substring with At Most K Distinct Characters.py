class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        slow, ans = 0, 0
        dct = {}
        
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = 1
            else:
                dct[s[i]] += 1
            
            while len(dct) > k:
                if dct[s[slow]] == 1:
                    del dct[s[slow]]
                else:
                    dct[s[slow]] -= 1
                slow += 1
            
            if len(dct) <= k:
                ans = max(ans, i - slow + 1)
        
        return ans