class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals:
            return []
        
        intervals.sort()
        result = [intervals[0]]
        
        for i in range(1,len(intervals)):
            temp = result.pop()
            
            if temp[1] < intervals[i][0]:
                result.append(temp)
                result.append(intervals[i])
            elif temp[1] >= intervals[i][0] and temp[1] < intervals[i][1]:
                result.append([temp[0], intervals[i][1]])
            elif temp[1] >= intervals[i][1]:
                result.append(temp)
            
        
        return result