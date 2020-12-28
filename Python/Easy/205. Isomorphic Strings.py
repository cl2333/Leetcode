class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        index_s, index_t = 0, 0
        dct_s, dct_t = {}, {}
        
        while index_s < len(s) and index_t < len(t):
            if s[index_s] not in dct_s and t[index_t] not in dct_t:
                dct_s[s[index_s]] = dct_s.setdefault(s[index_s], [index_s])
                dct_t[t[index_t]] = dct_t.setdefault(t[index_t], [index_t])
            elif s[index_s] in dct_s and t[index_t] in dct_t:
                if dct_s[s[index_s]] !=  dct_t[t[index_t]]:
                    return False
            else:
                return False
            
            index_s += 1
            index_t += 1
        
        return True
    
    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
        