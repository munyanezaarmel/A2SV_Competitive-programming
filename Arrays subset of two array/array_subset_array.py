def isSubset(a1, a2, n, m):
  
    freq_a1 = {}
    freq_a2 = {}
    

    for num in a1:
        freq_a1[num] = freq_a1.get(num, 0) + 1
    
    for num in a2:
        freq_a2[num] = freq_a2.get(num, 0) + 1
    

    for num, count in freq_a2.items():
        if num not in freq_a1 or freq_a1[num] < count:
            return "No"  
    
    return "Yes" 