class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        COLS = len(matrix[0])
        ROWS = len(matrix)

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False

        return True
