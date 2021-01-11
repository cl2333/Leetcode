class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter_p = dict(Counter(p))
        
        dct, result = {}, []
        k = len(p)
        for i in range(len(s)):
            dct[s[i]] = dct.get(s[i], 0) + 1
            
            if i >= k:
                if dct[s[i - k]] > 1:
                    dct[s[i - k]] -= 1
                else:
                    del dct[s[i - k]]
            
            if dct == counter_p:
                result.append(i - k + 1)
        
        return result

            
        