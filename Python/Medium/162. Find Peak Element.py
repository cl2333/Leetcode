class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        left, right = 0, len(nums) - 1 
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if nums[mid - 1] > nums[mid]:
                right = mid
            elif nums[mid] < nums[mid + 1]:
                left = mid
            else:
                return mid
        
        
        if nums[left] > nums[right]:
            return left
        else:
            return right