class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # Time Limit Exceeded
        # result = m
        # for i in range(m+1, n+1):
        #     result &= i
        # return result
        
        shift = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
            
        return m << shift
        