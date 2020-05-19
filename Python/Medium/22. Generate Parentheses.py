from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=deque([("",n,n)])
        
        for i in range(2*n):
            for i in range(len(result)):
                temp, left, right = result.popleft()
                if left > 0:
                    result.append((temp +'(',left-1,right))
                if right > left and right > 0:
                    result.append((temp + ')',left,right-1))
        
        return [i[0] for i in result]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, "", 0, 0, n)
        return res
        
    def backtrack(self, res, path, left, right, n):
        if right == n:
            res.append(path)
            return
        
        if left < n:    # can always add left '(' if available
            self.backtrack(res, path+'(', left+1, right, n)
        if left > right:
            self.backtrack(res, path+')', left, right+1, n)