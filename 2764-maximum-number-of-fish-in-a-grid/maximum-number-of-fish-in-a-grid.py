class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(start_r, start_c):
            # Initialize queue and visited set
            queue = deque([(start_r, start_c)])
            visited = set()
            visited.add((start_r, start_c))
            total_fish = 0
            
            while queue:
                r, c = queue.popleft()
                total_fish += grid[r][c]  # Catch all fish at this cell
                
                # Explore all four directions
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] > 0:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            
            return total_fish

        max_fish = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > 0:  # Start BFS from water cells only
                    max_fish = max(max_fish, bfs(r, c))
        
        return max_fish
            