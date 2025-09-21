class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # A sum of two numbers can be rearranged to as the sum minus the first number equals the second number
        # So we check this for each number in the list of possible second numbers
        # If not, store that number's possible second number in a dictionary
        # Then, for next number, check again if it is in the list of possible second numbers 
        possibleAddends={} 
        for i, num in enumerate(nums):
            if num in possibleAddends:
                return[i, possibleAddends[num]]
            addend = target - num
            if addend not in possibleAddends:
                possibleAddends[addend] = i
            
        