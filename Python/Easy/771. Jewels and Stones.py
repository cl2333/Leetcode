class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt=0
        for i in S:
            if i in J:
                cnt +=1
        return cnt

    def numJewelsInStones(self, J, S):
        return sum(map(J.count, S))