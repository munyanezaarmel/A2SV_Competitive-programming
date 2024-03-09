from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))

# Generate permutations
perm = permutations(arr)

for p in perm:
    split_index = len(arr) // 2
    first_half = p[:split_index]
    second_half = p[split_index:]

    sum_first_half = sum(first_half)
    sum_second_half = sum(second_half)

    if sum_first_half != sum_second_half:
        print(*p)
        break
else:
    print(-1)
