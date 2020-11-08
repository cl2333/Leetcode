class Solution:
    def numDecodings(self, s: str) -> int:
#         alphabet = [str(i) for i in range(1,27)]
        
#         def search(cur, s, result):
#             #print(s)
#             if s == "":
#                 result.append(cur)
            
#             for i in range(1,len(s)+1):
#                 if s[:i] in alphabet:
#                     search(cur + s[:i], s[i:], result)
        
#         result = []
#         search("", s, result)
        
#         return len(result)
        result = [0] * (len(s) + 1 )
        result[0] = 1
        if s[0] == '0':
            result[1] = 0
        else:
            result[1] = 1
        
        for i in range(2,len(s)+1):
            if 0 < int(s[i-1:i]) < 10:
                result[i] += result[i-1]
            
            if 10 <= int(s[i-2:i]) < 27:
                result[i] += result[i-2]
        
        return result[-1]
            