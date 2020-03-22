class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if not s:
            return True
        
        for i in s:
            if i in ['(', '{', '[']:
                stack.extend(i)
            if i == ')':
                if not stack or stack.pop() != '(':
                    return False
            if i == '}' :
                if not stack or stack.pop() != '{':
                    return False
            if i == ']' :
                if not stack or stack.pop() != '[':
                    return False
        
        return True and not stack 
                