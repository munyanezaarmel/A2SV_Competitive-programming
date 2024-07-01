class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = []
        def isValid(tmp):
            for i in range(1, len(tmp)):
                if tmp[i]  != tmp[i-1] - 1: 
                    return False
            return True
        def helper(i):
            if i >= len(s):
                if isValid(tmp):
                    return True
                return False
            for j in range(1, len(s)):
                if len(tmp) >= 2:
                    if tmp[-1] + 1 != tmp[-2]:
                        return False
                tmp.append(int(s[i: i+j]))
                if helper(i+j):
                    return True
                tmp.pop()
            return False        

        return helper(0)