class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1:
            return [-1,-1]
        
        l, r = 0, len(nums)-1
        while l < r:
            mid = int((l+r)/2)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        
        if nums[l] != target:
            return [-1,-1]
        
        left = 0 
        right = len(nums)-1
        
        while left < right:
            mid = int((left + right) /2 + 1)
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid 
            
            
        
        return[l,left]
        

# a clearer solution        
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def get_start_index(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid-1] != target:
                        return mid
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        def get_end_index(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start)//2
                if nums[mid] == target: 
                    if mid == len(nums)-1 or nums[mid + 1] != target:
                        return mid
                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1
        
        return [get_start_index(nums, target), get_end_index(nums, target)]