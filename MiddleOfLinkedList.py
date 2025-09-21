import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # First we find how many nodes there are using my findCount function by traversing until we reach the end
        # Then we get the median number if odd, if even, we get the second median node (middle 2nd)
        # Formula for median is, if even, divide by 2, and add 1 to get second middle
        # If odd, divide by 2, then round up
        tempHead = head
        count = self.findCount(tempHead)
        if(count % 2 == 0):
            count /= 2
            count + 1
        else:
            count /= 2
            math.ceil(count)
        iteration = 0
        while(iteration != count):
            head = head.next
            iteration += 1
        return head

    def findCount(self, head):
        count = 0
        while(head != None):
            head = head.next
            count += 1
        return count
        