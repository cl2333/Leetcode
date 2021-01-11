class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        
        for i, temp in enumerate(T):
            while stack and temp > stack[-1][0]:
                prev_i = stack.pop()[1]
                res[prev_i] = i - prev_i
            stack.append([temp, i])
            
        return res
        