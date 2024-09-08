# Definition for singly-linked list.
import math


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            return head
        n = 0
        temp = head
        while temp.next:
            n += 1
            temp = temp.next
        if n % 2 != 0:
            n += 1
        curr = head.next
        c = 1
        while curr.next and c <= math.ceil(n/2):
            val = curr.val
            temp1 = curr
            temp2 = curr.next
            while temp2:
                temp1.val = temp2.val
                temp2.val = val
                temp1 = temp1.next
                temp2 = temp2.next
            curr = curr.next
            c += 1
        return head

#Better way: store even and odd nums separately, then add heads at the end


sol = Solution()
res = sol.oddEvenList(ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))))
while res:
    print(res.val)
    res = res.next