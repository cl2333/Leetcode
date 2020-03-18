class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        ans = []
        loc = []
        
        for i, c in enumerate(S): 
            if c==C:
                loc.append(i) 
        
        
        for i in range(len(S)):
            ans.append(min([abs(i-j) for j in loc]))
        
        return ans
        