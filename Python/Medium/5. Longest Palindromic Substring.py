class Solution:
    def longestPalindrome(self, s: str) -> str:
        result ="" 
        for i in range(len(s)):
            result = max(result, self.find(s,i,i),key=len)
            result = max(result,self.find(s,i,i+1),key=len)
        return result    
    
    def find(self,s,left,right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
        