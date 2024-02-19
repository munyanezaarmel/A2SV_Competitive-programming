class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=[]
        for el in range(len(candies)):
            copy_array = candies[:]
            copy_array.pop(el)
            if candies[el]+extraCandies >= max(copy_array):
                result.append(True)
            else:
                result.append(False)
        return result
        