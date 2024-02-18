class Solution(object):
    def shuffle(self, nums, n):

        x=nums[0:n]
        y=nums[n:]
        result=[]
        i=0
        while i<n:
            result.append(x[i])
            result.append(y[i])
            i+=1
        return result

        