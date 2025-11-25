class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        stringLength = len(s)
        
        # In here, we loop through the possible substrings
        # We stop at half the length (//2) because a repeating pattern cannot be longer than half the string itself
        # Essentially firstSubstring is the lenght of the pattern we need to check per loop
        for firstSubstring in range(0, stringLength // 2):
            
            # We first determine the pattern we need to check, starting from the start up until the index loop + 1
            # Hence at start of loop, we check just the first character, at next, we check the first 2 characters, so on...
            pattern = s[0 : firstSubstring + 1]
            
            # We loop through the substring after the first substring
            # Our loop increments depending on the length needed
            # For example at loop 0, we have a & b,c,d,e,f
            # For example at loop 1, we have ab & cd, ef
            # But in this loop, we end at the last index + 1
            for nextSubstring in range(firstSubstring + 1, len(s), firstSubstring + 1):
                
                # If not a match, immediately stop
                if pattern != s[nextSubstring : nextSubstring + firstSubstring + 1]:
                    break
                
                # If it matches AND the index of the next substring plus firstsubstring 
                # (note this is also the length of the pattern) + 1 is equal to len(string)
                # nextSubString would be one pattern length plus 1 away from len(string)
                # Meaning it is the last pattern to be check
                elif (pattern == s[nextSubstring : nextSubstring + firstSubstring + 1] 
                      and nextSubstring + firstSubstring + 1 == stringLength):
                    return True # If so, return true, the string has a repeatedSubStringPattern within it
                    
        # If we try all possibilities and find no match
        return False