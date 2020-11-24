class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        start, end =  0, len(nums) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[end]:

                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                end -= 1
        
        if nums[start] == target:
            return True
        if nums[end] == target:
            return True
        
        return False       