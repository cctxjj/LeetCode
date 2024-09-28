# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        good_nodes = [root.val]
        self.analyse_good_nodes(root, root.val,good_nodes)
        return len(good_nodes)

    def analyse_good_nodes(self, start, prev_max, good_lst):
        if start.left:
            if start.left.val >= prev_max:
                good_lst.append(start.left.val)
            self.analyse_good_nodes(start.left, max(prev_max, start.left.val), good_lst)
        if start.right:
            if start.right.val >= prev_max:
                good_lst.append(start.right.val)
            self.analyse_good_nodes(start.right, max(prev_max, start.right.val), good_lst)
