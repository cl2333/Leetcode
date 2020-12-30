class Solution:
    def hIndex(self, citations: List[int]) -> int:
        tmp = [0] * (len(citations) + 1)
        for i in range(len(citations)):
            if citations[i] >= len(citations):
                tmp[len(citations)] += 1
            else:
                tmp[citations[i]] += 1
        
        count = 0
        for i in range(len(citations), -1, -1):
            count += tmp[i]
            if count >= i:
                return i
            
        return 0