# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = 0
        que = deque([(root, None, None)])
        while que:
            for _ in range(len(que)):
                node,parent, grand = que.popleft()
                if not node:
                    continue
                if parent and grand and grand.val %2 == 0:
                    ans += node.val
                que.append((node.left, node, parent))
                que.append((node.right, node, parent))
        return ans