n = int(input())
words = [input().strip() for _ in range(n)]

for word in words:
    length=len(word)
    changes=0
    if word==word[::-1]:
            print(0)
    else:
        for i in range(length//2):
            if word[i]!=word[length-i-1]:
                changes+=1
print(changes)


