class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        if len(costs[0]) == 1:
            return costs[0][0]
        
        result, tmp = [0] * len(costs[0]), [0] * len(costs[0])
        
        for cost in costs:
            for j in range(len(cost)):
                tmp[j] = min(result[:j] + result[j+1:]) + cost[j]
            result = tmp
            tmp = [0] * len(costs[0])
        
        return min(result)

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs: return 0
        n, k = len(costs), len(costs[0])
        for i in xrange(1, n):
            min1 = min(costs[i-1])
            idx = costs[i-1].index(min1)
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])
            for j in xrange(k):
                if j == idx:
                    costs[i][j] += min2
                else:
                    costs[i][j] += min1
        return min(costs[-1])