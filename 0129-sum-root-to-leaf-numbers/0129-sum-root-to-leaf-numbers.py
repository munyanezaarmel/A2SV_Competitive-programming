# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findNumbers(node, current_number):
            if not node:
                return 0
            current_number = current_number * 10 + node.val
            if node.left is None and node.right is None:
                return current_number
            return findNumbers(node.left, current_number) + findNumbers(node.right, current_number)
        
        return findNumbers(root, 0)
