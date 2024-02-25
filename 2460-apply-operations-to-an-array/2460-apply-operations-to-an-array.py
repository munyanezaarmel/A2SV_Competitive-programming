class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
                result.append(nums[i])
            else:
                 result.append(nums[i])
            i=i+1

        result.append(nums[-1])
        positive=[el for el in result if el>0]
        zeros=[el for el in result if el==0]
        return positive+zeros