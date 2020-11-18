from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        
        vocab = Counter(s)
        
        length = 0
        count_one = 1
        for char in vocab:
            if vocab[char] % 2 == 0:
                length += vocab[char]
            elif vocab[char] % 2 == 1 and count_one > 0:
                length += vocab[char]
                count_one = 0
            else:
                length += vocab[char] - 1
        
        
        return length
                
                
        