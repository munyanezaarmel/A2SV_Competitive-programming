n = int(input())

# Dictionary to store count and index of each file name
file_counts = {}

for _ in range(n):
    file_name = input()
    
    # If file_name is not in the dictionary, add it with count 1
    if file_name not in file_counts:
        file_counts[file_name] = 1
        print("OK")
    else:
        file_counts[file_name] += 1
        new_name = file_name + str(file_counts[file_name])
        print(new_name)
