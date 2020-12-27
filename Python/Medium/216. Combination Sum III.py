class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < k:
            return []
        result = []
        self.backtrack(list(range(1, min(n, 9) + 1)), 0, k, n, [], result)
        return result
    
    def backtrack(self, nums, index, k, target, cur, result):
        if len(cur) == k and target == 0:
            result.append(list(cur))
        
        if target <= 0:
            return
        
        for i in range(index, len(nums)):
            cur.append(nums[i])
            self.backtrack(nums, i+1, k, target - nums[i], cur, result)
            cur.pop()