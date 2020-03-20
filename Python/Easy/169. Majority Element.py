from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int: 
        c=Counter(nums)
        
        for i in c:
            if c[i] > len(nums)//2:
                return i