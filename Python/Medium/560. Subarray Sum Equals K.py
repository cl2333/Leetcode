class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        
        cur, ans = 0, 0
        for i in nums:
            cur += i
            ans += dct.get(cur - k, 0)
            dct[cur] = dct.get(cur, 0) + 1
                
        return ans