class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        left = []
        for i in range(n):
            left.append(i+1)
        return self.get_result([],left, k, [])    
    
    def get_result(self, begin, left, k, result):
        if len(begin) == k:
            result.append(begin)
            return result
        
        for i in range(len(left)):
            self.get_result(begin + [left[i]], left[i+1:], k, result)
        return result
        