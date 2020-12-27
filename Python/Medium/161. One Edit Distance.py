
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t or abs(len(s) - len(t)) > 1:
            return False
        
        index_s, index_t = 0, 0
        
        diff = 0
        while index_s < len(s) and index_t < len(t):
            if diff > 1:
                return False
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            else:
                diff += 1
                if len(s) > len(t):
                    index_s += 1
                elif len(s) < len(t):
                    index_t += 1
                else:
                    index_s += 1
                    index_t += 1
            
        return diff <= 1
        