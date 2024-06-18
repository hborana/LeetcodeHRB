class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()
        
        max_profit = 0  
        total_profit = 0  # Total profit we can achieve
        i = 0  # Job index
        
        for ability in worker:
            while i < len(jobs) and ability >= jobs[i][0]:
                max_profit = max(max_profit, jobs[i][1])
                i += 1
            total_profit += max_profit
        
        return total_profit
        