# Get input array size and elements
n = int(input())
arr = list(map(int, input().split()))

# Ensure distinct elements
if len(set(arr)) != n:
  print("Error: Array must contain distinct integers")
  exit()

# Initialize empty partitions
positive, negative, zero = [], [], []

# Partition based on sign and prioritize negative numbers
for num in arr:
  if num > 0:
    positive.append(num)
  elif num < 0:
    negative.append(num)
  else:
    zero.append(num)



# Print partition sizes and elements
print(len(negative),*negative)
print(len(positive), *positive)
print(len(zero), *zero)

