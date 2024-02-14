if __name__ == '__main__':
    N = int(input())
    result=[]
for element in range(N):
    commands=input().split()
    if commands[0] in "insert":
        result.insert(int(commands[1]),int(commands[2]))
    elif commands[0] in "append":
        result.append(int(commands[1]))
    elif commands[0] in "print":
        print(result)

    elif commands[0] in "pop":
        result.pop()
    elif commands[0] in "remove":
        result.remove(int(commands[1]))
    elif commands[0] in "sort":
       result.sort()
    elif commands[0] in "reverse":
       result.reverse()