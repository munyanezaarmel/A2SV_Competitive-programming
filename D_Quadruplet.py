n, target = map(int, input().split())
values = list(map(int, input().split()))

# Create a dictionary to store sums of pairs and their positions
pair_sums = {}

for i in range(n):
    for j in range(i + 1, n):
        pair_sum = values[i] + values[j]
        if pair_sum not in pair_sums:
            pair_sums[pair_sum] = (i + 1, j + 1)

for i in range(n):
    for j in range(i + 1, n):
        current_sum = values[i] + values[j]
        complement = target - current_sum
        if complement in pair_sums:
            a, b = pair_sums[complement]
            if a != i + 1 and a != j + 1 and b != i + 1 and b != j + 1:
                print(i + 1, j + 1, a, b)
                exit()

print("IMPOSSIBLE")
