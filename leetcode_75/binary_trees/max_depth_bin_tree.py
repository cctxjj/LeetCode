# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        roots = [root]
        depth = 0
        while roots:
            depth += 1
            new_roots = []
            for root in roots:
                if root.left:
                    new_roots.append(root.left)
                if root.right:
                    new_roots.append(root.right)
            roots = new_roots
        return depth
