# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        def build_balanced_bst(sorted_nodes):
            if not sorted_nodes:
                return None
            mid = len(sorted_nodes) // 2
            root = TreeNode(sorted_nodes[mid])
            root.left = build_balanced_bst(sorted_nodes[:mid])
            root.right = build_balanced_bst(sorted_nodes[mid+1:])
            return root
        
        sorted_nodes = inorder_traversal(root)
        
        return build_balanced_bst(sorted_nodes)
