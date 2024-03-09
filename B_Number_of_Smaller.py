n, m = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))
arr_3 = []

result=[]
first=0
for second in range(len(arr_2)):
    while first <len(arr_1) and arr_1[first]<arr_2[second]:
        first+=1
    result.append(first)
print(*result)
