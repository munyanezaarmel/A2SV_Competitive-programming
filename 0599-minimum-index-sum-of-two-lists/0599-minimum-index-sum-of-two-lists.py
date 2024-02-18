class Solution(object):
    def findRestaurant(self, list1, list2):
        dict={}
        for index,item in enumerate(list1):
            if item in list2:
                dict[item]= list2.index(item)+index
        min_value = min_value = min(dict.values())
        min_keys = [key for key, value in dict.items() if value == min_value]
        return min_keys
        