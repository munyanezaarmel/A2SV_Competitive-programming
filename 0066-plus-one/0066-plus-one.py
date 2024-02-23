class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=''.join(str(num) for num  in digits)
        add=int(n)+1
        result=[int(num) for num in str(add)]
        return result

        