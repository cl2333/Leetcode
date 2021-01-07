class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid
            else:
                left = mid
        
        if matrix[right][0] <= target:
            start_range = right
        elif matrix[left][0] <= target:
            start_range = left
        else:
            return False
             

        
        left, right = 0, len(matrix) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if matrix[mid][-1] == target:
                return True
            else:
                left = mid
                
        if matrix[right][-1] >= target:
            end_range = right
        elif matrix[left][-1] >= target:
            end_range = left
        else:
            return False
            
        
        if end_range < start_range:
            return False
        
        
        
        
        for i in range(start_range + 1):
            left, right = 0, len(matrix[0]) - 1
            while left + 1 < right:
                mid = left + (right - left) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid
                else:
                    left = mid
        
            if matrix[i][left] == target:
                return True
            if matrix[i][right] == target:
                return True

        return False
            

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if matrix:
            row,col,width=len(matrix)-1,0,len(matrix[0])
            while row>=0 and col<width:
                if matrix[row][col]==target:
                    return True
                elif matrix[row][col]>target:
                    row=row-1
                else:
                    col=col+1
            return False