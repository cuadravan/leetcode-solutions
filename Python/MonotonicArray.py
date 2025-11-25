import operator

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if(len(nums)<=2): # Any list with 2 elements are always monotonic (increasing or decreasing)
            return True
        
        i = 0 
        condition = None # First we loop through the list, determining if it should be increasing or decreasing, if it is break
        while(i < len(nums)-1): 
            if(nums[i] < nums[i+1]):
                condition = operator.le # If decreasing, we get the operation "less than or equal"
                break
            elif(nums[i] > nums[i+1]):
                condition = operator.ge # If increasing, we get the operation "greater than or equal"
                break
            i += 1
        # But if we have actually finished the loop earlier (no breaking), i should be at the end, meaning all elements are equal
        # It is monotonic then
        if(i == len(nums)-1):
            return True
        # Then we keep checking the condition we got earlier if it holds for the rest of the list
        for j in range(i, len(nums)-1):
            if(condition(nums[j], nums[j+1])):
                continue
            else:
                return False
        return True