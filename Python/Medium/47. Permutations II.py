class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = [False] * len(nums)
        result = []
        self.backtrack(nums, [], result, visited)
        return result
    
    def backtrack(self, nums, permutation, result, visited):

        if len(permutation) == len(nums):
            result.append(list(permutation))
        
        for i in range(len(nums)):
            if visited[i] == True or  (i>0 and nums[i] == nums[i-1] and visited[i-1] == False):
                continue
            
            visited[i] = True
            permutation.append(nums[i])
            self.backtrack(nums, permutation, result, visited)
            visited[i] = False
            permutation.pop()
        