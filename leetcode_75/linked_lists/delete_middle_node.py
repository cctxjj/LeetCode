# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        if head.next is None:
            return None

        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1

        target = math.ceil(n/2)
        temp = head
        prev = None
        for i in range(0, n):
            if i >= target:
                if temp.next is not None:
                  temp.val = temp.next.val
                else:
                    prev.next = None
            prev = temp
            temp = temp.next

        return head
