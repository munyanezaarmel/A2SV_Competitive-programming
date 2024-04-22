class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        for i in logs:
            if i == "../":
                if stack:
                    stack.pop()
            elif i == "./":
                continue
            else:
                stack.append(i)
        return len(stack)
            
        