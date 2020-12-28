class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        front, back = nums[0], nums[1]
        result = max(front, back)
        
        for i in range(2, len(nums)):
            tmp = max(front + nums[i], back)
            result = max(result, tmp)
            front = max(front, back)
            back = max(back, tmp)
        
        return result


class Solution:
    
    def rob(self, nums):
        
        last, now = 0, 0
        
        for i in nums: 
            last, now = now, max(last + i, now)
                
        return now