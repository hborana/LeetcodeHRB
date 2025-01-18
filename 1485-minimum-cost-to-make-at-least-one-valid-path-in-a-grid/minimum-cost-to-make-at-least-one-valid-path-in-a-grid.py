class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        # Direction mappings
        directions = {
            1: (0, 1),  # Right
            2: (0, -1), # Left
            3: (1, 0),  # Down
            4: (-1, 0)  # Up
        }
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0, 0)]  # (cost, x, y)
        
        # Cost matrix
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0
        
        while pq:
            curr_cost, x, y = heappop(pq)
            
            # If we reach the bottom-right cell
            if (x, y) == (m - 1, n - 1):
                return curr_cost
            
            # Skip if we already found a better way to this cell
            if curr_cost > cost[x][y]:
                continue
            
            # Explore all directions
            for direction, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny < n:  # Check bounds
                    new_cost = curr_cost + (grid[x][y] != direction)
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        heappush(pq, (new_cost, nx, ny))
        
        return -1  # Should never reach here if the grid is valid
