class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = float('inf')
        for i in range(len(prices)-1):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] > buy and prices[i+1] < prices[i]:
                result = result + prices[i] - buy
                buy = float('inf')
        
        if prices[-1] > buy:
            result = result + prices[-1] - buy
        
        return result
    
#Basically, if tomorrow's price is higher than today's, we buy it today and sell tomorrow. Otherwise, we don't. Here is the code:

class Solution(object):
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))