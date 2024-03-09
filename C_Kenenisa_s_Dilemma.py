n = int(input())  
arr = list(map(int, input().split())) 

swaps = [] 

for i in range(n):
    min_index = i 
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
    
    if min_index != i:
        swaps.append((i, min_index))
        arr[i], arr[min_index] = arr[min_index], arr[i]

print(len(swaps)) 
for swap in swaps:
    print(swap[0], swap[1])  
