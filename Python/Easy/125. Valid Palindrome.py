class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(e for e in s if e.isalnum()).lower()
        for i in range(0,int((len(s)+1)/2)):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
            