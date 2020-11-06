# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         def dfs(index, path, res):
#             res.append(path)
#             for i in range(index,n):
#                 if i>index and nums[i]==nums[i-1]:
#                     continue
#                 dfs(i+1, path + [nums[i]], res)
#         res = []
#         n = len(nums)
#         nums.sort()
#         dfs(0,[],res)
#         return res


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.search([], nums, result)
        return result
    
    def search(self, cur, nums, result):
        if cur not in result:
            result.append(cur)
        
        for i in range(len(nums)):
            self.search(cur+[nums[i]], nums[i+1:], result)
    
        

        
        