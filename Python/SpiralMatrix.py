class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # We need to determine first the boundaries of the matrix
        columnBoundary = len(matrix[0]) # For the columns, the boundary is the length of a specific column
        rowBoundary = len(matrix) # For row, the boundary is the length of the whole matrix is how many rows there are
        # The value of the boundary is +1 outside the normal index range
        
        
        # Note xLocation and yLocation corresponds to the the index of a 2d array [x][y]
        # Example positioning 
        # [0,0] [0,1] [0,2]
        # [1,0] [1,1] [1,2]
        # [2,0] [2,1] [2,2]
        # where [xLocation, yLocation]
        xLocation = 0
        yLocation = 0
        
        # We need to know the total number of elements, what we've already visited, how many we've visited, and the spiral matrix we need to make
        numberOfElements = columnBoundary * rowBoundary
        visited = set()
        elementsVisited = 0
        spiralMatrix = []
        
        # The order of the array is in a spiral, starting from the top left
        directionArray = ["Right", "Down", "Left", "Up"]
        directionIndex = 0
        
        # We loop until we have visited all elements
        while(elementsVisited < numberOfElements):
            
            # --- CRASH DETECTION ---
            # We check if our current coordinates (set by the previous loop) 
            # are Out of Bounds OR already in the Visited set.
            # If we have already visited the current x and y index, or if x and y are already at the boundary (which is outside the acceptable range)
            # Or if x and y index is illegal (-1)
            if((xLocation, yLocation) in visited or 
               (xLocation == rowBoundary or yLocation == columnBoundary or 
                xLocation == -1 or yLocation == -1)):
                
                # We add 2 to the direction index, this is a recovery direction move, if we were at Right, we now face Left
                # If we were at Down, we now move Up
                directionIndex += 2
                directionIndex %= 4 # To remain in the acceptable indices of the directionArray
                
                # We find out the x and y index we need to step into to recover
                xLocation, yLocation = self.traverse(xLocation, yLocation, directionIndex)
                
                # Then after we've recovered, we subtract one to the direction, which is the direction we need to step to continue the spiral
                directionIndex -= 1
                directionIndex %= 4
                
                # We find out the x and y index we need to step into to move forward
                xLocation, yLocation = self.traverse(xLocation, yLocation, directionIndex)

            # Add to the spiral matrix the value
            # Increment the elements visited
            # Add the current x and y index to the visited
            spiralMatrix.append(matrix[xLocation][yLocation])
            elementsVisited += 1
            visited.add((xLocation, yLocation))
            
            # No worries if we overextend, the recovery check in the next loop will save us
            xLocation, yLocation = self.traverse(xLocation, yLocation, directionIndex)
            
        return spiralMatrix

    def traverse(self, xLoc, yLoc, dirIndex):
        if(dirIndex == 0):   # Right
            yLoc += 1        
        elif(dirIndex == 1): # Down
            xLoc += 1
        elif(dirIndex == 2): # Left
            yLoc -= 1
        elif(dirIndex == 3): # Up
            xLoc -= 1
        return xLoc, yLoc