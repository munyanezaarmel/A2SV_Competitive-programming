class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        idKey -= 1
        self.stream[idKey] = value    
        result = []
        while self.ptr < len(self.stream):
            if self.stream[self.ptr] is not None:
                result.append(self.stream[self.ptr])
            else:
                break
            self.ptr += 1
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey, value)
