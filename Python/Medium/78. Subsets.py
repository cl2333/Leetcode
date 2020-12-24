class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        self.search(nums, 0, [], result)
        return result
    
    
    def search(self, nums, index, current, result):
        result.append(list(current))
        
        for i in range(index, len(nums)):
            current.append(nums[i])
            self.search(nums, i + 1, current, result)
            current.pop()
        