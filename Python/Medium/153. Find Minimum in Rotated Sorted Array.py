class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1
        while start + 1 < end:
           
            mid = start + (end - start) // 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid
        
        return min(nums[start], nums[end])