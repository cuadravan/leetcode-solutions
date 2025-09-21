class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Note here that we are traversing through the list, but we keep a separate pointer
        # This pointer only increments per unique number
        # Hence, everytime we see a unique number in the list, we add it at the pointer, then move the pointer rightwards
        # This ensures that all numbers from the left up until the leftPointer is unique
        # This continues until we iterated through the whole list
        # We return the number of unique elements, hence no need to decrement the leftPointer
        leftPointer = 0
        seenNums = {}
        for index, num in enumerate(nums):
            if num not in seenNums:
                seenNums[num] = 1
                nums[leftPointer] = num
                leftPointer += 1
        return leftPointer