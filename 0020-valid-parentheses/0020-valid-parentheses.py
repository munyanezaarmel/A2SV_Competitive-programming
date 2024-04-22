class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]

        all={")":"(","]":"[","}":"{"}

        for c in s:
            if c in all:
                if stack and stack[-1]==all[c]:
                    stack.pop()

                else:
                   return False
            else:
                stack.append(c)
        return True if not stack else False

