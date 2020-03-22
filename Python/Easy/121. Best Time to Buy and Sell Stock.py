class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p, max_p = inf, 0
        for p in prices:
            min_p=min(p, min_p)
            max_p=max(max_p, p-min_p)
        
        return max_p
        
        