from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # List of (capital, profit) tuples
        projects = list(zip(capital, profits))
        
        # Sort projects based on the required capital
        projects.sort(key=lambda x: x[0])
        
        # Min-heap for projects based on their required capital
        min_cap_heap = []
        # Max-heap for profits of the projects we can afford
        max_profit_heap = []
        
        # Index for the sorted projects
        i = 0
        n = len(projects)
        
        for _ in range(k):
            # Push all projects that can be started with the current capital to the max-heap
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_profit_heap, -projects[i][1])  # Use negative profit to simulate max-heap
                i += 1
            
            # If there are no projects that can be started, break
            if not max_profit_heap:
                break
            
            # Pop the most profitable project from the max-heap
            w += -heapq.heappop(max_profit_heap)
        
        return w
        