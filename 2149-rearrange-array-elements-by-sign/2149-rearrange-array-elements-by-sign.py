class Solution(object):
    def rearrangeArray(self, nums):
        negative= [el for el in nums if el<0]
        positive=[el for el in nums if el>0]

        result=[]

        for i in range(len(positive)):
                result.append(positive[i])
                result.append(negative[i])
        return result
        