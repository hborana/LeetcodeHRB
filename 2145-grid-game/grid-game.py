class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Calculate prefix sums for both rows
        top_prefix = [0] * n
        bottom_prefix = [0] * n
        top_prefix[0] = grid[0][0]
        bottom_prefix[0] = grid[1][0]
        
        for i in range(1, n):
            top_prefix[i] = top_prefix[i - 1] + grid[0][i]
            bottom_prefix[i] = bottom_prefix[i - 1] + grid[1][i]
        
        # Robot 1's strategy: minimize the maximum score Robot 2 can achieve
        result = float('inf')
        
        for i in range(n):
            # Points left on top after Robot 1 moves down at column i
            top_remaining = top_prefix[n - 1] - top_prefix[i]
            
            # Points left on bottom after Robot 1 moves to the right at column i
            bottom_remaining = bottom_prefix[i - 1] if i > 0 else 0
            
            # Robot 2's maximum score for this split
            max_robot2_score = max(top_remaining, bottom_remaining)
            
            # Robot 1 minimizes this maximum score
            result = min(result, max_robot2_score)
        
        return result