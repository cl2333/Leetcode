class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        begin, ans = 0, 0
        dct = {}
        
        for i in range(len(s)):
            if s[i] not in dct:
                dct[s[i]] = 1
            else:
                dct[s[i]] += 1
            
            
            while len(dct) > 2:
                if dct[s[begin]] > 1:
                    dct[s[begin]] -= 1
                else:
                    del dct[s[begin]]
                begin += 1
                
            if len(dct) <= 2:
                ans = max(ans, sum(dct.values()))
            
        return ans
                

        
                    
        