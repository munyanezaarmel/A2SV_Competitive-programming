n = int(input())

file_counts = {}

for _ in range(n):
    file_name = input()
    
    if file_name not in file_counts:
        file_counts[file_name] = 0
        print("OK")
    else:
        file_counts[file_name] += 1
        new_name = file_name + str(file_counts[file_name])
        print(new_name)
