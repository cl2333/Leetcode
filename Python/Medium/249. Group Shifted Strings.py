class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dct = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                diff = 26 + ord(s[i]) - ord(s[i - 1])
                key += (diff % 26,)
            dct[key] = dct.get(key, []) + [s]
        
        return list(dct.values())
        