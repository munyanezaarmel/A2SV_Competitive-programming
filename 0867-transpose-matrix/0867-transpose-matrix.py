class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows=len(matrix)
        cols=len(matrix[0])

        trasposed=[[0]*rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                trasposed[j][i]=matrix[i][j]

        return trasposed
  