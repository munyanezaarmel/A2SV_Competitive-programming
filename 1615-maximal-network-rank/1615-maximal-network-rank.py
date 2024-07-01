class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        
        adj = {i: set() for i in range(n)}
        for u, v in roads:
            adj[u].add(v)
            adj[v].add(u)

        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                # count total
                connected = len(adj[i]) + len(adj[j])

                # remove overlap
                if j in adj[i]:
                    connected -= 1

                res = max(res, connected)

        return res