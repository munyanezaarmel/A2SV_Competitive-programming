class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted=sorted(nums)

        result = []
        for index, value in enumerate(nums_sorted):
            if value == target:
                result.append(index)

        return result