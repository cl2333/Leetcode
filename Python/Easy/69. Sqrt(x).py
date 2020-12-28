#https://blog.csdn.net/u014485485/article/details/77599953?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
# #Newton iteration


class Solution:
    def mySqrt(self, x: int) -> int:
        
        # r = x
        # while r*r > x:
        #     r = (r + x/r) // 2
        # return int(r)
        
        l, r = 0, x
        while l + 1 < r:
            m = l + (r - l)//2
            
            if m * m > x:
                r = m
            elif m * m < x:
                l = m
            else:
                return m
        
        if r * r <= x:
            return r
        return l
        
        