
t = int(input())

for _ in range(t):
    s = input()

    if s == "abc" or s == "cba" or s=="bac":
        print("YES")
    else:
        if s[0] == 'a' :
            print("YES")
        else:
            print("NO")
