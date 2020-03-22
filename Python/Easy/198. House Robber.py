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

        # simpler version    
        last, now = 0, 0
        for i in nums: 
            last, now = now, max(last + i, now)  
        return now

        #another version lol
                if not nums:
            return 0
        if len(nums)<2:
            return nums[0]
        
        dp=[0]*len(nums)#define dp
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1]) 
        for i in range(2,len(nums)):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        print(dp)
        return dp[-1]