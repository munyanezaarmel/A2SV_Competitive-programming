class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        forward = [0]*len(arr)
        backward = [0]*len(arr)
        forward[0] = 1
        backward[-1] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                forward[i] = forward[i-1]+1
            else:
                forward[i] = 1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                backward[i] = backward[i+1]+1
            else:
                backward[i] = 1
        ans = 0
        for i in range(len(arr)):
            if forward[i]>1 and backward[i]>1:
                ans = max(ans, forward[i]+backward[i]-1)
        
        return ans