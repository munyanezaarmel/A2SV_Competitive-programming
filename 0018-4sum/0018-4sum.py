class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
                
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                    
                left = b + 1
                right = len(nums) - 1

                while left < right:
                    four_sum = nums[a] + nums[b] + nums[left] + nums[right]
                    if four_sum > target:
                        right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        result.append([nums[a], nums[b], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return result
