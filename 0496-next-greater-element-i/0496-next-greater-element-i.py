class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1Idx={n:i for i,n in enumerate(nums1)}
        res=[-1]*len(nums1)

        stack=[]

        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
               val=stack.pop()
               idx=nums1Idx[val]
               res[idx]=cur
            if cur in nums1Idx:
                stack.append(cur)

        return res
                
                
                
            