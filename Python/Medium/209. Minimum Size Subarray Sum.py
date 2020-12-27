class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        slow = 0
        sumation = 0
        length = len(nums) + 1
        for i in range(len(nums)):
            sumation += nums[i]
            
            while sumation >= s:
                length = min(i - slow + 1, length)
                sumation -= nums[slow]
                slow += 1
   
        return length if length < len(nums) + 1 else 0