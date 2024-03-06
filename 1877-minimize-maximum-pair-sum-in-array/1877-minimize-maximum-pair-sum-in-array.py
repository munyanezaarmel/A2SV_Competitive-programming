class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        first=0
        second=-1
        combined=[]
        while first<len(nums)//2:
                combined.append([nums[first],nums[second]])
                first+=1
                second-=1

        sums=[]
        for arr in combined:
                sums.append(sum(arr))
        return max(sums)

