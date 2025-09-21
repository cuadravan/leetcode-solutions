class Solution(object):
    def runningSum(self, nums):
        runningSumOutput = []
        runningSum = 0
        # Very simple problem, keep a running sum variable, keep adding it as we traverse the list and append the running sum to new list
        for num in nums:
            runningSum += num
            runningSumOutput.append(runningSum)
        return runningSumOutput
        