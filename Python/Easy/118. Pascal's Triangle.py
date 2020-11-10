class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(1,numRows+1):
            cur = [1] * i
            for j in range(1, i-1):
                cur[j] = result[-1][j-1] +  result[-1][j]
            result.append(cur)
        
        return result
        
        