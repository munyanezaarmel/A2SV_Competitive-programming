from collections import deque, defaultdict

class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)
        
        for u, v in redEdges:
            red_graph[u].append(v)
        for u, v in blueEdges:
            blue_graph[u].append(v)
        
        distances = [-1] * n
        
        queue = deque([(0, 'R', 0), (0, 'B', 0)])
        
        visited = set()
        visited.add((0, 'R'))
        visited.add((0, 'B'))
        
        while queue:
            node, last_color, dist = queue.popleft()
            if distances[node] == -1:
                distances[node] = dist
            
            if last_color == 'R':
                for neighbor in blue_graph[node]:
                    if (neighbor, 'B') not in visited:
                        visited.add((neighbor, 'B'))
                        queue.append((neighbor, 'B', dist + 1))
            else:
                for neighbor in red_graph[node]:
                    if (neighbor, 'R') not in visited:
                        visited.add((neighbor, 'R'))
                        queue.append((neighbor, 'R', dist + 1))
        
        return distances
