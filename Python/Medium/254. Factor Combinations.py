class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        self.backtrack([], n, result, 2)
        return result
    
    
    def backtrack(self, cur, n, result, start):
        if n == 1 and len(cur) > 1:
            result.append(list(cur))
        
        for i in range(start, n + 1):
            if n % i == 0 and i != 1:
                cur.append(i)
                self.backtrack(cur, n//i, result, i)
                cur.pop()