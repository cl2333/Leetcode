class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.find(sorted(candidates), target, [], [])
    
    def find(self, candidates, target, temp, ans):
        if target == 0:
            ans.append(temp)
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] <= target:
                self.find(candidates[i+1:], target - candidates[i], temp + [candidates[i]], ans )
        return ans
        