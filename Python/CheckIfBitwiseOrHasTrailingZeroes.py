class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Bitwise OR will have a trailing zero if both numbers are even (even means first bit from right is 0, so bitwise OR of 2 even numbers will result to zero at first bit from right)
        # Check if at least two elements are even
        # If so, then yes, this array has a combination whose bitwise OR has trailing zeroes
        evenCount = 0
        for index in range(len(nums)):
            if(nums[index]%2 == 0):
                evenCount += 1
            if evenCount == 2:
                break
        return True if (evenCount == 2) else False
        