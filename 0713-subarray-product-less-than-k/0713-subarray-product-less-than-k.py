class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        product=1
        l=0
        res=0

        for r in range(len(nums)):
            product*=nums[r]
      
            while l<=r and  product>=k:
                product=product//nums[l]
                l+=1
            res+=(r-l+1)

        return res