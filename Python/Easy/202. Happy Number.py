class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            seen.add(n)
            tmp = 0
            while n:
                tmp += (n%10)**2
                n = n//10
            
            if tmp in seen:
                return False
            
            n = tmp
        
        return True
            