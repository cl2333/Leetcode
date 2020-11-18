class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        
        
        
        left, right = 0, len(s) - 1 
        while left < right and right >=0 and left < len(s) :
            while left < len(s) and not s[left].isalnum():
                left += 1 
            while right >= 0 and not s[right].isalnum():
                right -= 1 
            
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -=  1
        
        return True
                