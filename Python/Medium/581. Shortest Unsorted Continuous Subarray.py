class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start_val, end_val = float('inf'), -float('inf')
        last = len(nums)
        
        
        res = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                start_val = min(start_val, nums[i])
                end_val = max(end_val, nums[i - 1])
                if  nums[i - 1] == end_val:
                    last = i
        
        start, end = len(nums), len(nums)
        for i in range(len(nums)):
            if nums[i] > start_val:
                start = min(start, i)
            if nums[i] >= end_val and i != start and i > last:
                end = min(end, i)
        
            
        
        if start_val != float('inf'):
            res = end - start 
        
        return res