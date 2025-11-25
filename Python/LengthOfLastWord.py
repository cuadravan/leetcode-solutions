class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastPointer = len(s)-1
        length = 0
        while(lastPointer!=-1):
            if(s[lastPointer]==" "):
                if(length != 0): # Meaning if we have already found a word beforehand, exit loop prematurely
                    break
            else:
                length += 1
            lastPointer -= 1
        return length
    # This is just essentially looping from the end of a string until we find a space, breaking from the loop and returning the length
            
        