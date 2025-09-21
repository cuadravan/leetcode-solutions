class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # If strs is empty, just return empty string (commonPrefix is empty from start)
        commonPrefix = ""
        if len(strs) == 0:
            return commonPrefix
        # Then we get the smallest length in the list of string
        minLength = len(min(strs))
        # If there is an empty string, again return empty string since only possible common prefix is empty string
        if minLength == 0:
            return commonPrefix
        # Then we check the list of strings by traversing each row simultaneously (note outer loop is iterating in each row)
        # Inner loop is iterating through each row
        # In essence we compare the nth element of each row with each other
        # We use minlength since it is the highest possible common prefix
        # Also note, we get the first row's element first, then get the rest of the row's elements one by one
        # This ensures no self comparison
        # If ever they aren't the same, return the commonPrefix (which is accumulation of common letters)
        # If it is wherein it has finished comparing with all other rows, add it to the commonPrefix (where it accumulates)
        # Continue until we compare all letters accordingly to the minimumLength of the prefix
        for letter in range(minLength):
            letterCheck = strs[0][letter]
            for word in range(1, len(strs)):
                if strs[word][letter] != letterCheck:
                    return commonPrefix
            commonPrefix += letterCheck
        return commonPrefix