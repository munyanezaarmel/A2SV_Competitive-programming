class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: 
            return ""
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return strs[0][:i]  
        return strs[0]  
