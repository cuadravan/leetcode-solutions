# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = self.getNumber(l1)
        num2 = self.getNumber(l2)
        sum = num1 + num2
        numberArray = str(sum)
        previous_node = None
        count = len(numberArray)
        for i in range(0,count):
            new_node = ListNode(int(numberArray[i]), previous_node)
            previous_node = new_node        
        return previous_node

    def getNumber(self, node):
        number = 0
        multiplier = 1
        while(node != None):
            number += node.val * multiplier
            multiplier *= 10
            node = node.next
        return number        