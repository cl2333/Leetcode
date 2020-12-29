class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)
        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)           
        # return max(dp)
        
        result = []
        for i in nums:
            pos = self.search(result, i)
            if pos == len(result):
                result.append(i)
            else:
                result[pos] = i
                
        return len(result)
        
        
    def search(self, result, val):
        if not result:
            return 0
        
        start, end = 0, len(result) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if result[mid] <= val:
                start =  mid
            else:
                end = mid
        
        if val <= result[start]:
            return start
        if val <= result[end]:
            return end
        return end + 1
        
            
         
        
        
                   