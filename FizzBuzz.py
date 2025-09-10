class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
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

        