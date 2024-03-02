class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        first = [el for el in str(abs(num))]  
        second = sorted(first) 
        second_first=second[:]
        negative = 0
        positive = 0

        if int(second[0]) == 0:
            for i in range(len(second)):
                 if int(second[i]) != 0:
                        second[0], second[i] = second[i], second[0]
                        break

        positive = int(''.join(second)) 

        third = second_first[::-1]  
        result = int("".join(third)) 
        negative = -result 

        if num > 0:
            return positive
        else:
            return negative

        