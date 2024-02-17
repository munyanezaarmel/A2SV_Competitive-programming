N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

pair_count = 0

count_b = {}
for value in b:
    count_b[value] = count_b.get(value, 0) + 1

for i in range(N): 
    for j in range(N): 
        matching_value = a[i] // c[j]  
        if matching_value in count_b:
            pair_count += count_b[matching_value]

print(pair_count)
