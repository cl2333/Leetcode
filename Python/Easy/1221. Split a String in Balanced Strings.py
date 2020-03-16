class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt=0
        flag=0
        
        for i in s:
            if i == 'R':
                flag += 1
            else:
                flag -= 1
            if flag == 0:
                cnt +=1
                
        return cnt


# simpler version
from itertools import accumulate as acc
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(acc(1 if c == 'L' else -1 for c in s)).count(0)