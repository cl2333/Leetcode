class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        self.findPalindrome(s, [], results)
        return results
    
    def findPalindrome(self, s, palindromes, results):
        if not s:
            results.append(list(palindromes))
        
        for i in range(len(s)):
            if not self.isPalindrome(s[:i+1]):
                continue
            palindromes.append(s[:i+1])
            self.findPalindrome(s[i+1:], palindromes, results)
            palindromes.pop()
            
    
    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True