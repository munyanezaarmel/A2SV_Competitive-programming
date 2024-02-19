class Solution(object):
    def largestPerimeter(self, nums):
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        for i in range(n - 1, 1, -1):
            if sorted_nums[i - 2] + sorted_nums[i - 1] > sorted_nums[i]:
                return sorted_nums[i - 2] + sorted_nums[i - 1] + sorted_nums[i]
        return 0
