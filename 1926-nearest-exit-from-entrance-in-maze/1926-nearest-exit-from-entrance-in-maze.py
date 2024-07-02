from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if (nx, ny) not in visited:
                        if (nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1) and (nx, ny) != (entrance[0], entrance[1]):
                            return steps + 1
                        queue.append((nx, ny, steps + 1))
                        visited.add((nx, ny))

        return -1