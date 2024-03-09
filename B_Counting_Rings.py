input_string = input()

count = 0
curr = 0

for char in input_string:
    if char == "O":
        count += 1
        curr = max(curr, count)
    else:
        count = 0

print(curr)
