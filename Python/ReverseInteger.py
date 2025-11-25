class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # For this one, first, we keep track of the sign of integer and make it positive
        # We get the multiplier of the highest digit since we are reversing it
        # We have a loop that exits if all digits of the number has been removed
        # In this loop, we first remove the rightmost digit, multiply it with the highest multiplier, then add to the reversedInteger
        # We then check if this overflows since it is a 32 bit integer in Python, we just check if it exceeds the boundary values
        # If so, note the overflow by returning 0
        # If not, remove the rightmost digit, and scale the multiplier down by 10 for the next digit
        # We return this integer with its original sign
        reversedInteger = 0
        negative = True if (x < 0) else False
        x = abs(x)
        multiplier = int(10 ** (self.countDigits(x)-1))
        while (x > 0):
            digit = x % 10
            reversedInteger += digit * multiplier
            if(self.checkOverflow(reversedInteger, negative)):
                return 0
            multiplier /= 10
            x //= 10
        if(negative):
            return -reversedInteger
        else:
            return reversedInteger

    def countDigits(self, x):
        if(x == 0):
            return 1
        else:
            count = 0
            while(x > 0):
                x //= 10
                count += 1
            return count

    def checkOverflow(self, x, negative):
        boundary = 2 ** 31
        if(negative == True):
            x *= -1
            return False if (x > -boundary) else True
        else:
            return False if (x < (boundary - 1)) else True