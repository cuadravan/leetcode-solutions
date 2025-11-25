class Solution:
    def judgeCircle(self, moves: str) -> bool:
        uCount = moves.count('U')
        dCount = moves.count('D')
        lCount = moves.count('L')
        rCount = moves.count('R')
        return uCount == dCount and lCount == rCount
        # A robot will always return to origin (considering it starts at origin) if its upward and downward cancel out, and its left and right movements cancel out