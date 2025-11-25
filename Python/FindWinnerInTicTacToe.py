class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        indexToPlayerDict = {0:"A", 1:"B"}
        playerMoves = [moves[0::2], moves[1::2]]
        # Player A moves first, in the list, the players move alternately, so from 1st element and then every other element
        # Player B moves next, same as above
        # We store the list of Player A moves as the first element, and the list of Player B moves as the second element
        # indexToPlayerDict allows us to return "A" or "B" depending on who satisfied the three check functions
        # If 0, "A" ; If 1 "B"
        # Then we do the checks, and return accordingly
        # But if none of the check works, then if there are 9 moves, it is a Draw since no more moves can be taken
        # If not yet 9 moves, then it is Pending as there are still moves
        print(playerMoves[0])
        for i in range(len(playerMoves)):
            if(self.diagonalCheck(playerMoves[i])):
                return indexToPlayerDict[i]
            if(self.verticalCheck(playerMoves[i])):
                return indexToPlayerDict[i]
            if(self.horizontalCheck(playerMoves[i])):
                return indexToPlayerDict[i]
        if(len(moves)<9):
            return "Pending"
        else:
            return "Draw"

    # The checks are a brute force way to check, we simply check if within the player's moves, they satisfy a specific order
    # The listed elements [x,y] correspond to moves and are mapped to a 3x3 grid
    def diagonalCheck(self, arr):
        if ([0,0] in arr and [1,1] in arr and [2,2] in arr):
            return True
        elif ([0,2] in arr and [1,1] in arr and [2,0] in arr):
            return True
        else:
            return False

    def horizontalCheck(self, arr):
        if ([0,0] in arr and [0,1] in arr and [0,2] in arr):
            return True
        elif ([1,0] in arr and [1,1] in arr and [1,2] in arr):
            return True
        elif([2,0] in arr and [2,1] in arr and [2,2] in arr):
            return True
        else:
            return False

    def verticalCheck(self, arr):
        if ([0,0] in arr and [1,0] in arr and [2,0] in arr):
            return True
        elif ([0,1] in arr and [1,1] in arr and [2,1] in arr):
            return True
        elif ([0,2] in arr and [1,2] in arr and [2,2] in arr):
            return True
        else:
            return False