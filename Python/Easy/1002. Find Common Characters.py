from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        n = Counter(A[0])
        ans = []
        for a in A[1:]:
            n = n & Counter(a)
        for i in n:
            ans.extend([i]*n[i])
        return ans
        # retrun list(n.elements())
    
    #without Counter
    def commonChars(self,A):
        check = list(A[0])
        for word in A:
            newCheck = []
            for c in word:
                if c in check:
                    newCheck.append(c)
                    check.remove(c)
            check = newCheck
        
        return check