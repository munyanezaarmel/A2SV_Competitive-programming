class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [-1] * n  
        
        def dfs(start):
            stack = [start]
            color[start] = 0  
            
            while stack:
                node = stack.pop()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                      
                        color[neighbor] = 1 - current_color
                        stack.append(neighbor)
                    elif color[neighbor] == current_color:
                    
                        return False
            return True
        
        for i in range(n):
            if color[i] == -1:
                if not dfs(i):
                    return False
        
        return True
