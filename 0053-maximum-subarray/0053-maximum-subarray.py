class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = [0] * len(nums)
        
        min_prefix_sum = prefix_sum[0]  
        
        prefix_sum[0] = nums[0]
        
        max_sum = float('-inf')
        
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
            
        for i in range(len(nums)):
            max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
            min_prefix_sum = min(min_prefix_sum, prefix_sum[i])  
                   
        return max_sum

        