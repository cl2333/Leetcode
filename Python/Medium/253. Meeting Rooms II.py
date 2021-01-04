from heapq import *

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        heap = []
        ans = 0
        for i in intervals:
            if heap and i[0] >= heap[0]:
                heapreplace(heap, i[1])
            else:
                heappush(heap, i[1])
            ans = max(ans, len(heap))
            
        return ans
            