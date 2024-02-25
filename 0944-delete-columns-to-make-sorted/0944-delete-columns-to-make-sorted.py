class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0
        
        for col in zip(*strs):  
            if list(col) != sorted(col):  
                count += 1
        
        return count
