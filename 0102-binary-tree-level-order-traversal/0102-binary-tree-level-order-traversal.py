from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        level = 0
        queue = deque([(root, 0)])
        currLevel = []

        while queue:
            node, nodeLevel = queue.popleft()

            if not node:
                continue

            if nodeLevel != level:
                levels.append(currLevel[:])  
                level += 1
                currLevel = []

            currLevel.append(node.val)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

        if currLevel:
            levels.append(currLevel[:])  

        return levels
