class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        min_heap = []
        
        # Add all boundary cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # Directions for moving in 4 neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        water_trapped = 0
        
        while min_heap:
            height, x, y = heapq.heappop(min_heap)
            
            # Check all 4 neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # If the neighbor is within bounds and not visited
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    # Water trapped on this neighbor is the difference between
                    # the current cell's height and the neighbor's height if positive
                    water_trapped += max(0, height - heightMap[nx][ny])
                    # Add the neighbor to the heap with the effective height
                    heapq.heappush(min_heap, (max(height, heightMap[nx][ny]), nx, ny))
        
        return water_trapped
