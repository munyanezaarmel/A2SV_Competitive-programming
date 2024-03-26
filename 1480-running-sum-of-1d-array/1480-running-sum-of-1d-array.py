class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        running_sums = [0] * n
        running_sums[0] = nums[0]
        for i in range(1, n):
             running_sums[i] = running_sums[i - 1] + nums[i]
        return running_sums