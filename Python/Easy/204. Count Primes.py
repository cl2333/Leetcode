class Solution:
    def countPrimes(self, n: int) -> int:
        
        count = 0
        prime = [True] * (n+1)
        
        for i in range(2, n):
            if prime[i]:
                count += 1
                
                j = 1
                while j * i <= n:
                    prime[i * j] = False
                    j += 1
        
        return count
        
            
        
        
        