# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        linked_list = []
        temp = head
        while temp:
            linked_list.append(temp.val)
            temp = temp.next

        biggest = linked_list[0] + linked_list[-1]
        for i in range(1, int(math.floor(len(linked_list)) - 1/2)):
            biggest = max(biggest, linked_list[i] + linked_list[len(linked_list) - 1-i])
        return biggest