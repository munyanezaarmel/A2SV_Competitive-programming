class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        running=count=0
        
        remainders=collections.defaultdict(int)
        
        remainders[0]=1
        
        for num in nums:
            
            running +=num
            
            if running%k in remainders:
                count+=remainders[running%k]
            
            remainders[running%k]+=1
        
        return count