class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Keep track of how many times array loops with step
        # Then we continuously modify number until it becomes zero, if even divide by 2, if odd minus 1. Each time, incrementing step.
        step = 0
        newNum = num
        while(newNum != 0):
            if(newNum % 2 == 0):
                newNum /= 2
                step += 1
            else:
                newNum -= 1
                step += 1
        return step