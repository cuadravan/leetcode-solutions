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
        