from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        c2=Counter(chars)
        ans=0
        
        for i in words:
            ci=Counter(i)
            flag=0
            
            for j in ci:
                if ci[j] <= c2.get(j,0):
                    flag +=1
            
            if flag == len(ci):
                ans += len(i)
        
        return ans
        
        #return sum(not cnt(w) - cnt(chars) and len(w) for w in words)