class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        size=len(chars)
        if size < 2:
            return size
        first=0
        second=0
        while first<size:
            count=1
            while first<size-1 and chars[first]==chars[first+1]:
                count+=1
                first+=1
                
            chars[second]=chars[first]
            second+=1
            if count>1:
                for val in str(count):
                    chars[second]=val
                    second+=1
            
            first+=1
            
        return second