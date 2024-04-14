class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        start_index = 0
        end_index = 1
        max_length = float('-inf')

        char_count = {}
        ch = word[0]
        char_count[ch] = 1

        while end_index < len(word):
            if word[end_index - 1] > word[end_index]:
                char_count.clear()
                start_index = end_index

            ch = word[end_index]
            char_count[ch] = char_count.get(ch, 0) + 1

            if len(char_count) == 5:
                max_length = max(max_length, end_index - start_index + 1)

            end_index += 1

        return max(max_length, 0)