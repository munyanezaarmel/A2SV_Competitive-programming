from collections import defaultdict

class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_counts = defaultdict(int)
        
        for a, b in trust:
            trust_counts[b] += 1
            trust_counts[a] -= 1
        
        for candidate in range(1, n + 1):
            if trust_counts[candidate] == n - 1:
                return candidate
        
        return -1
