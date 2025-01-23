class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
         # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Count the number of servers in each row and column
        row_counts = [0] * m
        col_counts = [0] * n
        
        # First pass: Calculate row and column counts
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    row_counts[i] += 1
                    col_counts[j] += 1
        
        # Second pass: Count the servers that can communicate
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (row_counts[i] > 1 or col_counts[j] > 1):
                    count += 1
        
        return count