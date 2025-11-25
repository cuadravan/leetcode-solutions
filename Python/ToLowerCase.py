class Solution:
    def toLowerCase(self, s: str) -> str:
        toLower = []
        for i in range(len(s)):
            if(65 <= ord(s[i]) <= 90):
                toLower.append(chr(ord(s[i])+32))
            else:
                toLower.append(s[i])
        return "".join(toLower) # Since toLower is a list of separate string (ex. "A", "B", "C") we need to join them into one string (ex. "ABC")
    # Using ASCII, we know that the decimal value of uppercase are within inclusive range of 65 and 90
    # Also, the lowercase equivalent of each letter is 32 above it (so that is why we add 32)