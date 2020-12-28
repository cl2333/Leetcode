import string

class Solution:
    def convertToTitle(self, n: int) -> str:
        dct = dict(zip(list(range(26)), string.ascii_uppercase))
        
        ans = ""
        while n > 0:
            num = (n - 1) % 26
            ans = dct[num] + ans
            n = (n - 1) // 26
        
        return ans
        
        