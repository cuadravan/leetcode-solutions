class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Essentially, from front and back of the string, we compare if they are equal or not
        # If equal, move both pointers (left is moved rightwards, right is moved leftwards)
        # If not equal, change the letter so that they are both the "lexicographically smaller" letter, this makes it a palindrome
        # Keep moving the pointers until firstPointer exceeds lastPointer, meaning it is already done checking all letters since it is now past the middle
        # We do a "".join since strList is a list and we need to return a string
        firstPointer = 0
        lastPointer = len(s)-1
        strList = list(s)

        while(firstPointer < lastPointer):
            if(s[firstPointer] != s[lastPointer]):
                if(strList[firstPointer] < strList[lastPointer]):
                    strList[lastPointer] = strList[firstPointer]
                else:
                    strList[firstPointer] = strList[lastPointer]
            firstPointer += 1
            lastPointer -= 1
        return "".join(strList)
        