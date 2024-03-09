n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

B = [[0]*m for _ in range(n)]

operations = []

for i in range(n-1):
    for j in range(m-1):
        if B[i][j] != A[i][j]:
            for x in range(i, i+2):
                for y in range(j, j+2):
                    if B[x][y] == 0:
                        B[x][y] = 1
                        operations.append((x+1, y+1))

match = True
for i in range(n):
    for j in range(m):
        if B[i][j] != A[i][j]:
            match = False
            break

if match:
    print(len(operations))
    for x, y in operations:
        print(x, y)
else:
    print(-1)
