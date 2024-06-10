class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            
            for i in range(len(remaining)):
                next_num = remaining[i]
                backtrack(path + [next_num], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return res
