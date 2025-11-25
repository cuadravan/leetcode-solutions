class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Keep track of how many times a letter appears using dictionary for O(1), key: value is letter:occurence
        # Then traverse ransom note and if decrement in the dictionary, the letter in ransom note
        # If it cannot be decremented anymore (reaches -1 if so) or if not in dictionary, we can't spell it so return False
        frequencyMap = {}
        for letter in magazine:
            if letter in frequencyMap:
                frequencyMap[letter] += 1
            else:
                frequencyMap[letter] = 1
        can_spell = True
        for letter in ransomNote:
            if letter in frequencyMap:
                if(frequencyMap[letter] > 0):
                    frequencyMap[letter] -= 1
                else:
                    can_spell = False
            else:
                can_spell = False
                break
        return can_spell

        