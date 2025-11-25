class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # To know if the parentheses are valid, we use a stack because it resembles how parentheses should work
        # When we open a parentheses, we push, and when we close with its corresponding parentheses, we pop
        # But if we push a parentheses, but pop it with something different, then we know it is not valid and return false
        if(len(s) % 2 != 0): # If not even, then it will never be valid since it cannot ever close properly
            return False
        closeParenthesesToOpen = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in range(0, len(s)):
            if(s[i]=="(" or s[i]=="[" or s[i]=="{"):
                stack.append(s[i])
            else:
                if(len(stack)!= 0 and stack[-1] == closeParenthesesToOpen[s[i]]):
                    stack.pop()
                else:
                    return False
        return True if (len(stack)==0) else False