class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=collections.defaultdict(int)
        res=0
        left_far=0
        left_near=0

        for r in range(len(nums)):
            count[nums[r]]+=1

            while len(count)>k:
                count[nums[left_near]]-=1
                if count[nums[left_near]]==0:
                    count.pop(nums[left_near])

                left_near+=1
                left_far=left_near

            while count[nums[left_near]]>1:
                count[nums[left_near]]-=1
                left_near+=1

            if len(count)==k:
                res+=left_near-left_far+1
        return res