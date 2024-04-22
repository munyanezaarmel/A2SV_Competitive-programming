class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        
        for s in s:
            if s=="*" and stack:
                stack.pop()
                
            else:
                stack.append(s)
                
        return "".join(stack)
            