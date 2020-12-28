import string
class Solution:
    def titleToNumber(self, s: str) -> int:
        dct = dict(zip(string.ascii_uppercase, list(range(1,27))))
        
        result = 0
        for i in s:
            result = result * 26 + dct[i]
        return result
        