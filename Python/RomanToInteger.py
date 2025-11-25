import math

class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntegerDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        integer = 0
        # Note that for Roman to Integer, 
        # I can be placed before V (5) and X (10) to make 4 and 9. 
        # X can be placed before L (50) and C (100) to make 40 and 90. 
        # C can be placed before D (500) and M (1000) to make 400 and 900.

        # Hence, my strategy here is to cycle through the Roman Numeral from left to right
        # previousRoman is set to infinity so that the first number always passes normally
        # Then, we use the romanToIntegerDict to map from Roman to Integer value
        # If that roman is greater than the previous roman (in case like IV, IX, XL, XC, CD, CM)
        # We multiply the previous roman by 2 and have that subtracted from the current roman
        # Why? Because the value of the two romans would be current Roman - previous Roman
        # But we did add the previous Roman earlier, that is why we multiply it by 2, to cancel that previous addition
        # Otherwise, normally the current Roman should always be lesser since it is arranged in decreasing order (except in special cases)

        previousRoman = math.inf
        
        for i in range(len(s)):
            currentRoman = romanToIntegerDict[s[i]]
            
            if currentRoman > previousRoman:
                integer += (currentRoman - previousRoman * 2)
            
            else:
                integer += currentRoman
            
            previousRoman = currentRoman
            
        return integer