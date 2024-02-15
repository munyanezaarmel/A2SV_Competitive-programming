class Solution:
    def check(self, A, B, N):
        count_A = {}
        count_B = {}

        for num in A:
            count_A[num] = count_A.get(num, 0) + 1

        for num in B:
            count_B[num] = count_B.get(num, 0) + 1

        return count_A == count_B
