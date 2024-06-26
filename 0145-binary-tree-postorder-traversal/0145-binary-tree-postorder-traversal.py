# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        left=self.postorderTraversal(root.left)
        
        right=self.postorderTraversal(root.right)
        
        curr=[root.val]
        
        result=left+right+curr
        
        return result