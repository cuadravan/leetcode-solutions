class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        for i in range(len(haystack)):
            if(needle == haystack[i:i+length]):
                return i
        return -1
    # We compare each possible substring with the length of needle inside haystack with our needle
    # Note that it is possible it would exceed, but this does not cause problems in Python
            