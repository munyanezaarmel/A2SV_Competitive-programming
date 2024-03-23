class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_elements=0
        for i in range(k):
            sum_elements+=nums[i]
         
        maxSum=sum_elements
        
        startIndex=0
        endIndex=k
        
        while endIndex<len(nums):
            sum_elements-=nums[startIndex]
            startIndex+=1
            
            sum_elements+=nums[endIndex]
            endIndex+=1         
            maxSum=max(maxSum,sum_elements)
        
        return float(maxSum)/k