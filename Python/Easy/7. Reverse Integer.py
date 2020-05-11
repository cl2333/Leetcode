class Solution:
    def reverse(self, x: int, flag = 0) -> int:
        y=0
        while x >0:
            y=y*10+x%10
            x=x//10
            
        if x <0:
            x=-x
            while x >0:
                y=y*10+x%10
                x=x//10
            y=-y
        if y < -2**31 or x < -2**31 or y > 2**31-1 or x > 2**31-1:
            return 0
        return y
        
        
        