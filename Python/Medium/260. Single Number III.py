from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result = []
        for v, freq in counter.items():
            if freq == 1:
                result.append(v)
        
        return result
        