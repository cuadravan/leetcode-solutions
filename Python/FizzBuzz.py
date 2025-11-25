class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Given a number, we start from 1 until we reach that number
        # For every number, if divisible by 3, we add Fizz
        # If divisible by 5, we add Buzz (but we add to the same string since both conditions can be true)
        # But if it is blank, we just add the number (this cannot be true with both previous conditions also true since it is not a number)
        # Then we append the resulting string from this iteration, then move on to next number
        output = []
        number = 1
        while number <= n:
            string = ""
            if(number % 3 == 0):
                string += "Fizz"
            if(number % 5 == 0):
                string += "Buzz"
            if(string == ""):
                string += str(number)
            output.append(string)
            number += 1
        return output

        