n,h=map(int,input().split())
friends=list(map(int,input().split()))
sum=0
for el in friends:
    if el<=h:
        sum+=1
    else:
        sum+=2
print(sum)