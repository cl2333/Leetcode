class Solution:
    def addBinary(self, a: str, b: str) -> str:
        index_a, index_b = len(a)-1, len(b)-1
        
        num = 0
        result = ''
        
        while num > 0 or index_a >= 0 or index_b >=0:
            if index_a >=0:
                num += int(a[index_a])
                index_a -=1
                
            if index_b >=0:
                num += int(b[index_b])
                index_b -=1
            
            result =  str(num%2) + result
            
            num //= 2 
        
        
        return result