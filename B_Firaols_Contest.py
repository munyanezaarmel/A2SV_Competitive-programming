n, m = map(int, input().split())
problems = list(map(int, input().split()))
difficult = set()
rounds = []
for problem in problems:
    difficult.add(problem)
    if len(difficult) == n:
        rounds.append(1)
        difficult.clear()  
    else:
        rounds.append(0)
result=''.join(map(str, rounds))
print(result)
