n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

for i in range(n):
    if i % 2 == 0:
        nums[i] = sorted_nums[i // 2]
    else:
        nums[i] = sorted_nums[-((i + 1) // 2)]

print(*nums)