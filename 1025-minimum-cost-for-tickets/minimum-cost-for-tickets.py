class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # Use a set for quick lookup of travel days
        day_set = set(days)
        max_day = days[-1]  # The last travel day
        dp = [0] * (max_day + 1)

        for i in range(1, max_day + 1):
            if i not in day_set:  # If not a travel day, cost remains the same as the previous day
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],  # 1-day pass
                    dp[max(0, i - 7)] + costs[1],  # 7-day pass
                    dp[max(0, i - 30)] + costs[2]  # 30-day pass
                )

        return dp[max_day]