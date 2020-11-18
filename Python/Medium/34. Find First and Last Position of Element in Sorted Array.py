class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        start, end = 0, len(nums) - 1
        end_index = -1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                start = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[end] == target:
            end_index = end
        elif nums[start] == target:
            end_index = start
         
        if end_index == -1:
            return [-1, -1]
        
        start = end_index
        while start >= 0 and nums[start] == nums[end_index]:
            start -= 1
        
        return [start + 1, end_index]
    
        