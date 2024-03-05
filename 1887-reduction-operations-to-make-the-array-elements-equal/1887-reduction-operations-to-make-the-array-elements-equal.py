class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count =0
        total = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += 1
            total += count
        return total