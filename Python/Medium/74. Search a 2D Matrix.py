class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [] or matrix[0] == []: 
            return False
        
        begin, end = 0, len(matrix)-1
        
        while begin <= end:
            mid = (begin + end) // 2
            
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                begin = mid+1
        
        row = end
        begin, end = 0, len(matrix[0])-1
        
        while begin <= end:
            mid = (begin + end) // 2
            
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                begin = mid + 1
        
        if matrix[row][end] == target:
            return True
        
        
        return False
        
                
        
        