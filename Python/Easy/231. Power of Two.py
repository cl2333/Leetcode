class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return 0
        while n % 2 == 0:
            n = n // 2
        return n == 1

        if n <= 0:
            return False
        return !n&(n-1)
        