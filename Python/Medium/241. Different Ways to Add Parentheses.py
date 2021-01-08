class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        result = []
        
        if "+" not in input and "-" not in input and "*" not in input:
            return [int(input)]
        
        for i, v in enumerate(input):
            if v == "+" or v == "-" or v == "*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                
                for l in left:
                    for r in right:
                        if v == "+":
                            result.append(l + r)
                        if v == "-":
                            result.append(l - r)
                        if v == "*":
                            result.append(l * r)
        
        return result
                            