class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd=[]
        even=[]
        
        for i in A:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
                
        return even+odd

# simpler version
return([i for i in A if i%2==0]+[i for i in A if i%2!=0])

return sorted(A, key=lambda x: x % 2)