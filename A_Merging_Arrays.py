n, m = map(int, input().split())
arr_1 = list(map(int, input().split()))
arr_2 = list(map(int, input().split()))



# n=6
# m=7
# arr_1=[1 ,6 ,9 ,13, 18, 18]
# arr_2=[2 ,3 ,8 ,13 ,15, 21 ,25]
#
result=[]
#
# """
# 1 2 3 6 8 9 13 13 15 18 18 21 25
#
# """
first=0

second=0

while first < n and second < m:
    if arr_1[first]<arr_2[second]:
        result.append(arr_1[first])
        first+=1
    else:
        result.append(arr_2[second])
        second+=1

result.extend(arr_1[first:])
result.extend(arr_2[second:])
print(*result)






