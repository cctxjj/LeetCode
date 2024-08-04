# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_1 = self.nodeToList(l1)
        list_2 = self.nodeToList(l2)

        num_1 = ''
        num_2 = ''
        for element in list_1:
            num_1 = num_1 + str(element)

        for element in list_2:
            num_2 = num_2 + str(element)

        result = str(int(num_1) + int(num_2))
        solution = []
        len_res = len(result)
        for i in range(0, len_res):
            solution.append(result[len_res-1-i])

        return self.listToNode(solution)

    def nodeToList(self, node):
        curr_node = node
        result = []
        while curr_node is not None:
            result.append(curr_node.val)
            curr_node = curr_node.next
        result.reverse()
        return result

    def listToNode(self, inp):
        result = ListNode(val=inp[0], next=None)
        curr_node = result
        for element in inp[1:]:
            new_node = ListNode(val=element, next=None)
            curr_node.next = new_node
            curr_node = new_node
        return result



