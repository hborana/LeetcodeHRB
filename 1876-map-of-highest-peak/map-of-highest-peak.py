class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()
        
        # Initialize the queue with all water cells and set their height to 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))
        
        # Directions for moving to adjacent cells
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Perform BFS
        while queue:
            x, y = queue.popleft()
            current_height = height[x][y]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and height[nx][ny] == -1:
                    height[nx][ny] = current_height + 1
                    queue.append((nx, ny))
        
        return height
            