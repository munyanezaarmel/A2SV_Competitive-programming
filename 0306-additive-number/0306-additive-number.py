class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        
        # Helper function to validate the sequence
        def validate_sequence(start):
            length = len(sequence)
            if start == n:
                return length >= 3 and all(sequence[i] == sequence[i-1] + sequence[i-2] for i in range(2, length))
            
            for end in range(start + 1, n + 1):
                segment = num[start:end]
                if segment.startswith('0') and len(segment) > 1:
                    break
                number = int(segment)
                if length < 2 or number == sequence[-1] + sequence[-2]:
                    sequence.append(number)
                    if validate_sequence(end):
                        return True
                    sequence.pop()
            return False

        sequence = []
        return validate_sequence(0)

