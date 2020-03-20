class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums)<3:
            return max(nums)
        
        money = [nums[0], nums[1]]
        
        for i  in range(2,len(nums)):
            money=[max(money[0],money[1]),money[0]+nums[i]]
            
        return max(money)
            
        last, now = 0, 0
        for i in nums: 
            last, now = now, max(last + i, now)  
        return now