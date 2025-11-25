class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        sDict = {}
        tDict = {}
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = 1
            else:
                sDict[s[i]] += 1
            if t[i] not in tDict:
                tDict[t[i]] = 1
            else:
                tDict[t[i]] += 1
        return True if (sDict == tDict) else False
    # To determine if t is an anagram of s, we get the frequency dictionaries of both s and t, then check if they are equal
    # If equal, then it is an anagram