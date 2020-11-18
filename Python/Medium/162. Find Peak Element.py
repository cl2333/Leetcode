class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1 
        
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] <= nums[start]:
                end = mid
            elif nums[mid] > nums[start] and nums[mid] <= nums[end]:
                start = mid
            else:
                if nums[mid - 1] < nums[mid]:
                    start = mid
                elif nums[mid - 1] > nums[mid]:
                    end = mid
        
        if nums[start] < nums[end]:
            return end
        else:
            return start
        