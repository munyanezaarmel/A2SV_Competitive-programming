class Solution(object):
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []