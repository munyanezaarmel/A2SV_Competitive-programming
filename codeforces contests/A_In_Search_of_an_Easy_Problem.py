def Search(n, responses):
    if 1 in responses:
        return "HARD"
    else:
        return "EASY"

n = int(input()) 
responses = list(map(int, input().split()))  

result = Search(n, responses)
print(result)
