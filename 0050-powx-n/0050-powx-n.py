class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n == 1: return x
        if n == -1: return 1 / x
        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        return (self.myPow(x, n // 2) ** 2) * x
    
    