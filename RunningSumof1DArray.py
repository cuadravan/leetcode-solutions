class Solution(object):
    def runningSum(self, nums):
        runningSumOutput = []
        runningSum = 0
        for num in nums:
            runningSum += num
            runningSumOutput.append(runningSum)
        return runningSumOutput
        