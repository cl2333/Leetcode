class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i, j = 0, len(A)-1
        k = len(A) - 1
        ans = [0] * len(A)
        
        while i <= j:
            if (-A[i]) > A[j]:
                ans[k] = A[i] ** 2
                k -=1
                i +=1
            else:
                ans[k] = A[j] ** 2
                k -=1
                j -=1
                
        return ans

        #return sorted([i**2 for i in A])