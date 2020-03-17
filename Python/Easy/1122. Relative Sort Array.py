from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        c1 = Counter(arr1)
        ans = []
        diff = []
        
        for i in arr2:
            ans.extend([i]*c1[i])
            
        for i in arr1:
            if i not in arr2:
                diff.append(i)
        diff.sort()
        
        return ans+diff

        #simpler version
        c2={i:j for j,i in enumerate(arr2)}
        return sorted(arr1,key=lambda a : c2.get(a,1000+a))