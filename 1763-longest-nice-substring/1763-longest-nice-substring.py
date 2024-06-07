class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """                
        if len(s)==1 or len(s)==0:
            return ""
        nice=""
        for window in range(2,len(s)+1):
            for i in range(len(s)-window+1):
                string=s[i:window+i]
                #print(string)
                s1=set(string)
                s2=set(string.swapcase())
                s1=s1-s2
                if len(s1)==0:
                    if len(nice)<len(string):
                        nice=string
                
        return nice