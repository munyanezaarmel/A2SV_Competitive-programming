if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max1=max(arr)
    new_arr=[arr[x] for x in range(len(arr)) if arr[x]!=max1]
    print(max(new_arr))
    
    