class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        ans = []
        self.backtrack(nums, [], ans, visited)
        return ans
    
    def backtrack(self, nums, permutation, ans, visited):
        if len(permutation) == len(nums):
            ans.append(list(permutation))
        
        for i in nums:
            if i in visited:
                continue
            visited.add(i)
            permutation.append(i)
            self.backtrack(nums, permutation, ans, visited)
            visited.remove(i)
            permutation.pop()
        
