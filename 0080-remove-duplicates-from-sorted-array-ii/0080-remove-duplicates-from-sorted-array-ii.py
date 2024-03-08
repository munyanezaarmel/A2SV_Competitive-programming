class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 1
        second = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
               count+=1
            else:
                count=1
            if count<=2:
                nums[first]=nums[i]
                first+=1
        return first
        
        
        