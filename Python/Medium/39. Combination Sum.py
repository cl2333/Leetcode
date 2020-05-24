class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.find(sorted(candidates), target, [], [])
    
    def find(self, candidates, target, temp, ans):
        if target == 0:
            ans.append(temp)
        
        for i in range(len(candidates)):
            if candidates[i] <= target:
                self.find(candidates[i:], target - candidates[i], temp + [candidates[i]], ans )
        return ans
        