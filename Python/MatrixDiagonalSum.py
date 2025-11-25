class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonalSum = 0
        for i in range(len(mat)):
            diagonalSum += mat[i][i]

        end = len(mat)-1
        for i in range(len(mat)):
            if(i != end):
                diagonalSum += mat[i][end]
            end -= 1

        return diagonalSum
    # Note that the index [i][i] of an array are all in a diagonal direction (from top left to bottom right)
    # So we loop through these to get the first diagonal
    # To traverse the second diagonal, we need the index of the bottom left which should be equal to [0][len(arr)-1]
    # To start traversing the second diagonal from bottom left to top right, we simply add the firstIndex and subtract the secondIndex
    # But note, we skip if first Index and second Index are equal, because we already calculated that in the first Diagonal

        