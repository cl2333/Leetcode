class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.search([], nums, 0, result)
        return result
    
    def search(self, cur, nums, index, result):
        result.append(list(cur))
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            cur.append(nums[i])
            self.search(cur, nums, i+1, result)
            cur.pop()
    
        

        
        