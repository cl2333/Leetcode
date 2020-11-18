class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return False
    
        left, right = self.find_diff(0, len(s) - 1, s)
        if left >= right:
            return True
        
        return self.is_Palindrome(left + 1, right, s) or self.is_Palindrome(left, right - 1, s) 
    
    
    def is_Palindrome(self, left, right, s):
        left, right = self.find_diff(left, right, s)
        if left >= right:
            return True
        else:
            return False
        
        
    def find_diff(self, left, right, s):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return left, right