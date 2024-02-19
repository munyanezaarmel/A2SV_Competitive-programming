n, q = map(int, input().split())
words = input().split()

for _ in range(q):
    pref, suff = input().split()
    result = -1  
    for i, word in enumerate(words):
        if word.startswith(pref) and word.endswith(suff):
            result = i  
    print(result)
