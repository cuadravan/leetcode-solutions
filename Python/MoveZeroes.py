class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        newIndexDict = {}
        newIndex = 0
        for i in range(len(nums)): # We loop through the list of integers
            if(nums[i] != 0): # If not zero
                newIndexDict[newIndex] = nums[i] # We store the non-zero element with its key as its future index (from the start it is zero, but we increment every time we add a non-zero element)
                nums[i] = 0 # We turn that element to zero
                newIndex += 1 # We increment the future index for the next non-zero element
        for i in range(newIndex): # We simply loop over how many times we get non-zero elements
            nums[i] = newIndexDict[i] # And setting the values with their keys or index within the dictionary
        # Essentially, set everything to zero, but store the non-zero elements with their new index, then put them back into the list using the new index
