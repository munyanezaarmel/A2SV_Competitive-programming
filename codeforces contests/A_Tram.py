n = int(input())
array = []
result = []


for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))
count = 0
for i in range(n):
    count = count - array[i][0] + array[i][1]
    result.append(count)

print(max(result))
