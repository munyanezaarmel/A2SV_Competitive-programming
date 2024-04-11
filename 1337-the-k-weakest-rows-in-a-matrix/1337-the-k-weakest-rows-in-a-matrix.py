class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        ROWS = len(mat)
        COLS = len(mat[0])
        result = []

        for row in range(ROWS):
            count = 0
            for col in range(COLS):
                if mat[row][col] == 1:
                    count += 1
            result.append([row,count])
            row_strength = []
            for i, row in enumerate(mat):
                count = sum(row)
                row_strength.append((count, i))

            row_strength.sort()
            result=[i for _, i in row_strength[:k]]

        return result