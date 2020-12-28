class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1, d2 = {}, {}
        
        for i, val in enumerate(pattern):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(s.split()):
            d2[val] = d2.get(val, []) + [i]
        
        return sorted(d1.values()) == sorted(d2.values())
        