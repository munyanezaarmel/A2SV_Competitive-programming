class Solution(object):
    def decodeString(self, s):
        def helper(s, i):
            decoded = ''
            num = 0
            while i < len(s):
                if s[i].isdigit():
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    i, inner_decoded = helper(s, i + 1)
                    decoded += inner_decoded * num
                    num = 0
                elif s[i] == ']':
                    return i, decoded
                else:
                    decoded += s[i]
                i += 1
            return decoded

        return helper(s, 0)