from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1  # Base case: 1 way to achieve sum 0
        
        for num in nums:
            next_dp = defaultdict(int)
            for s, count in dp.items():
                next_dp[s + num] += count  # Add the current number
                next_dp[s - num] += count  # Subtract the current number
            dp = next_dp  # Move to the next state
        
        return dp[target]