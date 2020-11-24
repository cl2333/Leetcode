class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter = {}
        count = 0
        for a in A:
            for b in B:
                counter[a+b] = counter.get(a+b, 0) + 1
        
        for c in C:
            for d in D:
                if -(c+d) in counter:
                    count += counter[-(c+d)]
        
        return count