class Solution(object):
    def pivotArray(self, nums, pivot):
        less=[nums[el] for el in range(len(nums)) if nums[el]<pivot]
        greater=[nums[el] for el in range(len(nums)) if nums[el]>pivot]
        equal=[nums[el] for el in range(len(nums)) if nums[el]==pivot]
        merged=[less,equal,greater]
        flattened_list = [element for sublist in merged for element in sublist]
        return flattened_list
        