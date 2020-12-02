class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.find(sorted(candidates), 0, target, [], results)
        return results
    
    def find(self, candidates, index, target, combination, results):
        if target == 0:
            results.append(list(combination))
        if target < 0:
            return 
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            combination.append(candidates[i])
            self.find(candidates, i+1, target - candidates[i], combination, results)
            combination.pop()
        