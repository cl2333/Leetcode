class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.backtrack(sorted(nums), 0, len(nums), [], [])
    
    def backtrack(self, nums, index, target, temp, ans):
        if index == target:
            ans.append(temp)
        
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if i < len(nums)-1:
                self.backtrack(nums[:i]+nums[i+1:], index+1, target, temp+[nums[i]], ans)
            else:
                self.backtrack(nums[:i], index+1, target, temp+[nums[i]], ans)
        
        return ans