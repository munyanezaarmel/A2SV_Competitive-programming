class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        def backtrack(index, distribution):
            if index == len(cookies):
                current_unfairness = max(distribution)
                self.min_unfairness = min(self.min_unfairness, current_unfairness)
                return

            for i in range(k):
                distribution[i] += cookies[index]
                
                if distribution[i] < self.min_unfairness:
                    backtrack(index + 1, distribution)
                
                distribution[i] -= cookies[index]
        
        self.min_unfairness = float('inf')
        backtrack(0, [0] * k)
        
        return self.min_unfairness
