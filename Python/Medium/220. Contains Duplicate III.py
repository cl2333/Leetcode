class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        
        n = len(nums)
        d = {}
        w = t + 1
        
        for i in range(n):
            m = nums[i] // w
            if m in d:
                return True
            if m - 1 in d and abs(d[m - 1] - nums[i]) <= t:
                return True
            if m + 1 in d and abs(d[m + 1] - nums[i]) <= t:
                return True
            
            d[m] = nums[i]
            
            if i >= k:
                del d[nums[i - k] // w]
            
        return False
            
        