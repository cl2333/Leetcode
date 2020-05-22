class Solution:
    def countAndSay(self, n: int) -> str:
        if n==0:
            return ""
        s = "1"
        for i in range(1,n):
            count, temp = 1, ""
            for j in range(1,len(s)):
                if s[j] == s[j-1]:
                    count += 1
                else:
                    temp += str(count) 
                    temp += s[j-1]
                    count = 1
            temp += str(count) 
            temp += s[-1]
            s = temp
        return s
            
        
            
            