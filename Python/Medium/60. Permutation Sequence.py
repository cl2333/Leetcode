class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        string = "".join([str(i+1) for i in range(n)])
        resultList = self.getResult('',string, [])
        return resultList[k-1]
        
    def getResult(self, begin, left, result):
        if left == '':
            result.append(begin)
            return result
        for i in range(len(left)):
            if i == len(left)-1:
                self.getResult(begin+left[i], left[:i],result)
            else:
                self.getResult(begin+left[i], left[:i]+left[i+1:],result)
        return result

# Timeout Error


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials, nums = [1], ['1']
        for i in range(1, n):
            factorials.append(factorials[i-1]*i)
            nums.append(str(i+1))
        
        k -= 1
        
        result = ''
        for i in range(n):
            idx = k // factorials[-1]
            result += nums[idx]
            k = k%factorials[-1]
            del factorials[-1]
            del nums[idx]
        
        return result