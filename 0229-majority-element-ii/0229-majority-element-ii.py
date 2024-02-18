class Solution(object):
    def majorityElement(self, nums):
        index=len(nums)//3
        numbers={}
        result=[]
        for i  in range(len(nums)):
                numbers[nums[i]]=numbers.get(nums[i],0)+1
        for key,value in numbers.items():
                    if value>index:
                        result.append(key)
        return result
        