class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # It is essentially a variable length sliding window where the right pointer keeps moving forward until it sees a duplication
        # In my code, we iterate through the list
        # If the new letter is UNIQUE or if it is "not unique but it is right behind the left pointer" meaning not anymore in the sliding window
        # We add that letter and its index in the dictionary
        # Otherwise, this means that letter is duplicating and within the current sliding window
        # Move sliding window's left pointer to after the already seen duplicating character, then update the seen duplicating character's index in dict
        # This way, the just seen unique character is now the only one in the sliding window
        # We get the max length for every iteration, then keep moving the right pointer forward to check the next letter
        seenLetter = {}
        length = 0
        maxLength = 0
        leftPointer = 0
        rightPointer = 0
        for i, letter in enumerate(s):
            # If we haven't seen the letter yet OR
            # If the repeating character is outside the window
            if letter not in seenLetter or seenLetter[letter] < leftPointer:
                seenLetter[letter] = i # We add it to seen letter / update it to its new index
            
            # If the repeating character is already seen and inside the window
            else:
                # Adjust left pointer to after the repeating character
                leftPointer = seenLetter[letter] + 1 
                # Update repeating character's index
                seenLetter[letter] = i
            # Get the max length so far    
            length = rightPointer - leftPointer + 1
            maxLength = length if length > maxLength else maxLength
            # Move the right pointer forward
            rightPointer += 1               
        return maxLength