from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dct = Counter(s)
        
        count = 0
        for value in dct.values():
            if count > 1:
                return False
            if value % 2 == 1:
                count += 1
        
    
        return count <= 1