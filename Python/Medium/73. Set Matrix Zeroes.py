class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        #O(m+n) space
        row_index = [False] * len(matrix)
        col_index = [False] * len(matrix[0])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_index[i] = True
                    col_index[j] = True
        
        for i in range(len(matrix)):
            if row_index[i] == True:
                matrix[i] = [0] * len(matrix[0])
        
        for i in range(len(matrix[0])):
            if col_index[i] == True:
                for j in range(len(matrix)):
                    matrix[j][i] = 0



        #O(1) space
        row_0, col_0 = False, False
        
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                row_0 = True
        
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                col_0 = True
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1,len(matrix[0])):
                    matrix[i][j] = 0
        
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1,len(matrix)):
                    matrix[i][j] = 0
        
        if col_0 :
            for i in range(len(matrix)):
                matrix[i][0] = 0
        
        if row_0 :
            for j in range(len(matrix[0])):
                matrix[0][j] = 0       
        
                    
                    
            