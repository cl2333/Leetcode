class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        result = 0
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] < target - nums[i]:
                    result += (right - left)
                    left += 1
                else:
                    right -= 1
        
        return result