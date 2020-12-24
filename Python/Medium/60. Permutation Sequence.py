
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n+1))
        fact = [1] * n
        for i in range(1, n):
            fact[i] = i * fact[i-1]
        
        result = ""
        for i in range(n-1, -1, -1):
            n = (k-1) // fact[i]
            result += str(nums[n])
            nums.pop(n)
            k = k%fact[i]
            
        
        return result
        
            
        