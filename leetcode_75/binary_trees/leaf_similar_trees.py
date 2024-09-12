# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        arr_1 = []
        arr_2 = []
        self.get_leaves(root1, arr_1)
        self.get_leaves(root2, arr_2)
        return arr_1 == arr_2


    def get_leaves(self, root, arr):
        if root is None:
            return
        if root.left is None and root.right is None:
            arr.append(root.val)
        else:
            if root.left is not None:
                self.get_leaves(root.left, arr)
            if root.right is not None:
                self.get_leaves(root.right, arr)

