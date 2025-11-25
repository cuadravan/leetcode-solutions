class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        self.addOne(digits, len(digits)-1) # We call the recusrive function with last element
        return digits # Return digits, note we manipulate digits by reference
    def addOne(self, digits, indexToAdd): # This is a recursive function
        if digits[indexToAdd] == 9: # If the number we are adding one to is 9
            digits[indexToAdd] = 0 # Set that as 0
            if indexToAdd == 0: # If its index is already the leftmost, we add a 1 to its left 
                digits.insert(0, 1)
            else: # Otherwise, call this same function but with the index to the left
                self.addOne(digits, indexToAdd - 1)
        else: # If the number we are adding one to is not 9, just add 1 to it
            digits[indexToAdd] += 1
            