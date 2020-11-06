class Solution:
    def grayCode(self, n: int) -> List[int]:
        results = [0]
        
        for i in range(n):
            results += [v + 2**i for v in results[::-1]]
        
        return results