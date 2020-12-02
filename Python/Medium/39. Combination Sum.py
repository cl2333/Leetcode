class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.find(sorted(list(set(candidates))), 0, target, [], results)
        return results
    
    def find(self, candidates, index, target, combination, results):
        if target == 0:
            results.append(list(combination))
        if target < 0:
            return 
        
        for i in range(index, len(candidates)):
            combination.append(candidates[i])
            self.find(candidates, i, target - candidates[i], combination, results)
            combination.pop()
