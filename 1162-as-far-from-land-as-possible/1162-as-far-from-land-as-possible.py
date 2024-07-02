from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if not n:
            return -1

        queue = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        if len(queue) == 0 or len(queue) == n * n:
            return -1
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        max_distance = -1

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    grid[nx][ny] = grid[x][y] + 1
                    max_distance = max(max_distance, grid[nx][ny])
                    queue.append((nx, ny))
        
        return max_distance - 1

