class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        # Initialize the DP array
        dp = [0] * (high + 1)
        dp[0] = 1  # Base case: One way to form an empty string
        
        # Populate the DP array
        for i in range(high + 1):
            if dp[i] > 0:
                if i + zero <= high:
                    dp[i + zero] = (dp[i + zero] + dp[i]) % MOD
                if i + one <= high:
                    dp[i + one] = (dp[i + one] + dp[i]) % MOD
        
        # Count the good strings
        return sum(dp[low:high + 1]) % MOD