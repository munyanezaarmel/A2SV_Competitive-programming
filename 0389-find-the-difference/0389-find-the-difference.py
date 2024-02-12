class Solution(object):
    def findTheDifference(self, s, t):
        
        c=Counter(s)
        d=Counter(t)
        for char,item in d.items():
            if char not in d or item !=c[char]:
                return char

          
            
        