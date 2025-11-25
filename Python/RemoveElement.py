class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # First we determine where the lastPointer should be
        lastPointer = len(nums)-1

        # Edge cases where there is only one element
        if len(nums) == 1:
            if nums[0] == val:
                return 0
            else:
                return 1

        # Keep track of how many non-value elements there are
        validNums = 0
        # Iterate through the list
        for firstPointer in range(len(nums)):
            # If the number at our first pointer should be removed (equal to value)
            if nums[firstPointer] == val:
                # We find the ideal spot from the back (not equal to value)
                while(nums[lastPointer] == val):
                    lastPointer -=1
                    # But if we end up going past the front, it means no more valid swaps
                    # so return now the number of valid numbers (not equal to value)
                    if(lastPointer <= firstPointer):
                        return validNums
                # If we find the ideal swap from front element to back element, we swap
                temp = nums[firstPointer]
                nums[firstPointer] = nums[lastPointer]
                nums[lastPointer] = temp
            # Each time we iterate from the front, it is a valid number
            # It will have been swapped or skipped
            validNums += 1
                

        