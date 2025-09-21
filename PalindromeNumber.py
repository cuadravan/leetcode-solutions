class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # If negative, it is never a palindrome due to the negative sign
        if(x < 0):
            return False
        # We count how many digits there are
        listDigit = [d for d in str(x)]
        multiplier = 10 ** (len(listDigit) - 1)
        tempNum = x
        reversedNumber = 0
        # Then we get rightmost digit, multiply it with highest multiplier, and add it to reversedInteger
        # Then remove rightmost digit and scale down multiplier
        while(tempNum > 0):
            digit = tempNum % 10 # Get the last digit
            reversedNumber += (digit * multiplier)
            multiplier /= 10
            tempNum //= 10
        # If they are equal, it is a palindrome number 
        return True if (x == reversedNumber) else False 