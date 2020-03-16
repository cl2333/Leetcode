class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n=str(n)
        
        sum_n=0
        mul_n=1
        
        for i in str_n:
            sum_n += int(i)
            mul_n *= int(i)
            
        return mul_n - sum_n
        
        