class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans, max_prod, min_prod = nums[0], nums[0], nums[0]
        
        for num in nums[1:]:
            x = max(num, max_prod * num, min_prod * num)
            y = min(num, max_prod * num, min_prod * num)
            max_prod, min_prod = x, y
            ans = max(ans, max_prod)
        
        return ans
        