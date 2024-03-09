# Function to construct the matrix
def construct_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    num = 1
    for i in range(n):
        matrix[i][i] = num
        num += 1

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                if i % 2 == 0:
                    matrix[i][j] = num
                else:
                    matrix[i][n-1-j] = num
                num += 1

    return matrix

# Input the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Input the size of the matrix
    n = int(input())
    # Construct the matrix
    matrix = construct_matrix(n)
    # Print the matrix
    for row in matrix:
        print(*row)
