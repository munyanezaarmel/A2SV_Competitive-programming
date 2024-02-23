class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        
        reversed_words = reversed(words)
        
        reversed_string = ' '.join(reversed_words)
        
        return reversed_string
