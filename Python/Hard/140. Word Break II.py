class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         if not s:
#             return []
        
#         max_len = max([len(word) for word in wordDict]) if wordDict else 0
        
#         result = []
        
#         def backtrack(cur, s):
#             if s == "":
#                 result.append(" ".join(cur[::-1]))
            
#             for l in range(1, max_len + 1):
#                 if l > len(s):
#                     break
                
#                 word = s[len(s) - l:] 
#                 if word not in wordDict:
#                     continue
                
#                 cur.append(word)
#                 backtrack(cur, s[:len(s) - l])
#                 cur.pop()       
        
#         backtrack([], s)
#         return result
        
        
        if not s:
            return []
        
        max_len = max([len(word) for word in wordDict]) if wordDict else 0
        
        result = []
        memo = {}
        
        def backtrack(s):
            if s == "":
                return [[]]
            
            if s in memo:
                return memo[s]
            
            res= []
            for l in range(1, max_len + 1):
                if l > len(s):
                    break
                
                word = s[len(s) - l:] 
                if word not in wordDict:
                    continue
                
                last_res = backtrack(s[:len(s) - l])
                res += [i + [word] for i in last_res]
        
            memo[s] = res
            return res
        
        return [" ".join(i) for i in backtrack(s)]
        
                
    