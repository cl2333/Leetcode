class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        result = []
        self.get_result(nums, 0, [], result, k)
        return result
    
    def get_result(self, nums, index, cur, result, k):
        if len(cur) == k:
            result.append(list(cur))
        
        for i in range(index, len(nums)):
            cur.append(nums[i])
            self.get_result(nums, i + 1, cur, result, k)
            cur.pop()
            
        