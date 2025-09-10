class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
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

        