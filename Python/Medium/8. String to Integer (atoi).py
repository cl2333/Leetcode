class Solution:
    def myAtoi(self, str: str) -> int:
        
        
        ls=list(str.strip())
        if len(ls)==0:
            return 0
        
        if ls[0]=='-':
            sign= -1
        else:
            sign=1
        
        if ls[0] in ['+','-']:
            del ls[0]
        num,i=0,0
        while i < len(ls) and ls[i].isdigit():
            num=num*10+ord(ls[i]) - ord('0')
            i=i+1
        return min(2**31-1,max(sign*num,-2**31))