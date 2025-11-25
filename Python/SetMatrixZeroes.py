class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 0):
                    matrix[i][j] = None # For every 0 we find, we set it to None as an in-place flag

        # Traverse matrix again to find the flags
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == None):
                    # If we find the flag, first traverse that element's rows [0,0] [0,1] [0,2], note that first position index is constant but the second position index depends on the row's length
                    for k in range(len(matrix[i])):
                        # We do this to avoid overwriting the flag, since we need it to check all possible rows and columns
                        matrix[i][k] = 0 if matrix[i][k] != None else matrix[i][k]
                    # Then traverse that element's column [0,0] [1,0] [2,0], note that second index position is constant but the first position index depends on the matrix's length or number of rows
                    for k in range(len(matrix)):
                        matrix[k][j] = 0 if matrix[k][j] != None else matrix[k][j]

        # Now we set all the flags to 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == None):
                    matrix[i][j] = 0

        