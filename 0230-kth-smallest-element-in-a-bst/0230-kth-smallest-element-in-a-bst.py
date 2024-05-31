# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node):
            if not node:
                return 
            
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            inorder(node.right)
        
        self.k, self.res = k, None
        inorder(root)
        return self.res