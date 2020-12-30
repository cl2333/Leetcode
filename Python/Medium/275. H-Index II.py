class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        
        low, high = 0, len(citations) - 1
        while low + 1 < high:
            mid = low + (high - low) // 2
            h = len(citations) - mid
            if citations[mid] >= h:
                if mid - 1 >= 0 and citations[mid - 1] >= h + 1:
                    high = mid
                else:
                    return h
            else:
                low = mid
        
        if citations[low] >= len(citations) - low:
            return len(citations) - low
        if citations[high] >= len(citations) - high:
            return len(citations) - high
        
        return 0
                