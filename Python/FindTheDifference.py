class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        currentLetters = {}
        for i in range(len(s)):
            if s[i] not in currentLetters:
                currentLetters[s[i]] = 1
            else:
                currentLetters[s[i]] += 1
        for i in range(len(t)):
            if t[i] in currentLetters and currentLetters[t[i]] >= 1:
                currentLetters[t[i]] -= 1
            else:
                return t[i]
        # In here, we first make a frequency dictionary by traversing through the list first
        # Then, we traverse the second string, but we subtract if the letter is found in the frequency dictionary
        # If it is not found, OR if the frequency of a letter cannot anymore be subtracted (or it is 0), then that is the difference between the 2 strings