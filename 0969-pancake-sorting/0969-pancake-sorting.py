class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        x=len(arr)
        k=[]
        for i in range(x):
            max_n=max(arr[:x-i])
            max_i=arr.index(max_n)+1
            arr[:max_i]=reversed(arr[:max_i])
            k.append(max_i)
            arr[:x-i]=reversed(arr[:x-i])
            k.append(x-i)
        return k
    