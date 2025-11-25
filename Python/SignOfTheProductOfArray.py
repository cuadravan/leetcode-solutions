class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if(0 in nums):
            return 0
        nums.sort()
        negativeCount = 0
        for i in range(len(nums)):
            if(nums[i] > 0):
                break
            else:
                negativeCount += 1
        negative = True if (negativeCount%2 != 0) else False
        return -1 if negative else 1
        # If there is a zero, the result of the elements multiplied is always zero
        # To determine if the product is negative, it must have an odd number of negatives