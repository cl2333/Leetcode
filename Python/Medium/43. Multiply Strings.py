class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        mapping = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        
        
        int1 = []
        int2 = []
        
        for i in num1:
            int1.append(mapping[i])
        for i in num2:
            int2.append(mapping[i])
        
        return str(self.convertInteger(int1)*self.convertInteger(int2))
    
    
    def convertInteger(self, num):
        return sum( v*10**i for i, v in enumerate(num[::-1]))
        