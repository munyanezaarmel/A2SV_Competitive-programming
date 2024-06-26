# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        def constructTree(root1, root2):
            if not root1 and not root2:
                return None
            if not root2:
                return root1
            if not root1:
                return root2
            head = TreeNode(root1.val + root2.val)
            head.left = constructTree(root1.left, root2.left)
            head.right = constructTree(root1.right, root2.right)
        
            return head
        
        return constructTree(root1, root2)
