class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # I define here an array that follows a counter-clockwise order North -> West -> South -> East
        # +1 would mean turning left, and -1 would mean turning right
        directionArray = ["North", "West", "South", "East"]
        directionIndex = 0 # Starts facing North
        
        xLocation = 0 # This stores where they are right now, which is at origin
        yLocation = 0
        
        for i in range(len(instructions)):
            if instructions[i] == "G":
                # Move based on current facing direction
                match directionArray[directionIndex]:
                    case "North":
                        yLocation += 1
                    case "South":
                        yLocation -= 1
                    case "West":
                        xLocation -= 1
                    case "East":
                        xLocation += 1
                        
            elif instructions[i] == "L":
                # If L, turn Left, so we move forward in the array or add 1 (0 -> 1 -> 2 -> 3 -> 0)
                directionIndex += 1
                directionIndex %= 4
                
            elif instructions[i] == "R":
                # If R, turn Right, we move backward in array or subtract 1
                # If -1, it becomes 3 (modulo)
                directionIndex -= 1
                directionIndex %= 4

        # If we are at origin, we did come at full circle
        # If we are not facing north, we will eventually move in a circle after more attempts
        # This is because if we face left, next movement will make us face left again, then left again, then left again. Hence a circle.
        # If we face right, same happens.
        # If we face down, we technically cancel the movement after just 2. We face down, then from there we face down again. We are back where we started.
        return (xLocation == 0 and yLocation == 0) or (directionArray[directionIndex] != "North")