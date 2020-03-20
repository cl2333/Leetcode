class Solution:
    def climbStairs(self, n: int) -> int:

        if n<3:
            return n
        
        ways = [1,2]
        
        for i in range(3,n+1):
            ways=[ways[1],ways[0]+ways[1]]
        
        return ways[1]