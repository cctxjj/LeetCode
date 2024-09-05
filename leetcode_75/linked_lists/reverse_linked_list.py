# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        return self.listToNode((self.nodeToList(head))[::-1])

    def nodeToList(self, node):
        result = []
        while node is not None:
            result.append(node.val)
            node = node.next
        return result

    def listToNode(self, input_list):
        first_node = ListNode(input_list[0])
        pointer_node = first_node
        for element in input_list[1:]:
            pointer_node.next = ListNode(element)
            pointer_node = pointer_node.next
        return first_node