class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        res = 0
        cnt = 0
        
        for i in nums:
            if i:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0

        return max(cnt, res)
        