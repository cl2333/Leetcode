class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n <0:
            x = 1/x
            n = -n
        return self.fastPow(x, n)
        
        
    def fastPow(self, x, n):
        if n == 0:
            return 1
        
        half = self.fastPow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x



class Solution(object):
    def __init__(self):
        self.cache = {}

    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1.0/self.helper(x, -n)
        return self.helper(x, n)

    def helper(self, x, n):
        if n in self.cache:
            return self.cache[n]
        if n == 1:
            return x
        left = n/2
        right = n-left
        temp = self.helper(x, left) * self.helper(x, right)
        self.cache[n] = temp
        return temp