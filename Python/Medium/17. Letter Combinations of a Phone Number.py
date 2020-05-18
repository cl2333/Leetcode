from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or digits == '1':
            return []
        mapping = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        result = deque([''])
        for i in digits:
            if i == 1:
                continue
            index_i = int(i)-2
            n = len(result)
            for j in range(n):
                temp = result.popleft()
                for k in mapping[index_i]:
                    result.append(temp+k)
        
        return result
            
#simplified solution
def letterCombinations(self, digits):
    dict = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7': "pqrs", 
        '8':"tuv", '9':"wxyz"}
    cmb = [''] if digits else []
    for d in digits:
        cmb = [p + q for p in cmb for q in dict[d]]
    return cmb

#backtracking
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]