class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
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