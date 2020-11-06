class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
#         result = [[]]
        
#         for i in nums:
#             result += [r + [i] for r in result]
        
#         return result

        result = []
        self.search([], nums, result)
        return result
    
    
    def search(self, current, nums, result):
        result.append(current)
        
        for i in range(len(nums)):
            self.search(current+[nums[i]], nums[i+1:], result)
        