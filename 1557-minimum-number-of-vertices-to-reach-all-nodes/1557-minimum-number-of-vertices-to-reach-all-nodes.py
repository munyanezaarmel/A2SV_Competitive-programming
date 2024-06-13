class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        endVert = {}
        startVert = {}
        for edge in edges:
            startVert[edge[0]] = 1
            endVert[edge[1]] = 1
        ans = []
        for start in startVert:
            if start not in endVert:
                ans.append(start)
        return ans