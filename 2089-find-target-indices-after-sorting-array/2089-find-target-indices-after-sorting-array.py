class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                 if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        result = []
        for index, value in enumerate(nums):
            if value == target:
                result.append(index)

        return result