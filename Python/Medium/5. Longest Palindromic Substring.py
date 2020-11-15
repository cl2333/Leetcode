class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
#         result = (0, 0)
#         for mid in range(len(s)):
#             result = max(result, self.isPalindrome(mid, mid, s))
#             result = max(result, self.isPalindrome(mid, mid+1, s))
  
#         return s[result[1]:result[1]+result[0]]
        
#     def isPalindrome(self, left, right, s):
#         while left >= 0 and right < len(s) and  s[left] == s[right]:
#             left -= 1
#             right += 1
#         return (right-left-1, left+1)

#dynamic programming
        length = len(s)
        is_Palindrome = [[False] * length for _ in range(length)]
        
        for i in range(length):
            is_Palindrome[i][i] = True
        for i in range(1, length):
            is_Palindrome[i][i-1] = True
        
        start, longest = 0, 1
        for string_length in range(2, length+1):
            for begin in range(0, length - string_length + 1):
                end = begin + string_length - 1
                if is_Palindrome[begin+1][end-1] == True and s[begin] == s[end]:
                    is_Palindrome[begin][end] = True
                    longest = string_length
                    start = begin
             
        return s[start:start+longest]