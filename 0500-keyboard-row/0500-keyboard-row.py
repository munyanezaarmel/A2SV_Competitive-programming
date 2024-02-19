class Solution(object):
    def findWords(self, words):
        row_1 = "qwertyuiop"
        row_2 = "asdfghjkl"
        row_3 = "zxcvbnm"
        result = []

        for word in words:
            lowercase_word = word.lower()
            if all(char in row_1 for char in lowercase_word) or \
               all(char in row_2 for char in lowercase_word) or \
               all(char in row_3 for char in lowercase_word):
                result.append(word)

        return result
