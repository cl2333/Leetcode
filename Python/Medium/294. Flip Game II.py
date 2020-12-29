class Solution:
    def canWin(self, s: str) -> bool:
        flag = False
        return self.backtrack(s, flag)
    
    
    def backtrack(self, s, flag):
        if not "++" in s:
            return False
        
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                flag = flag or not self.backtrack(s[:i] + "--" + s[i + 2:], flag)
            if flag:
                return True
        return False
        