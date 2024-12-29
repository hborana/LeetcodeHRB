class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(words), len(words[0])
        t_len = len(target)
        
        # Precompute the frequency of each character at each position in the words
        freq = [[0] * 26 for _ in range(n)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1

        # DP table: dp[i][j] means ways to form first i chars of target using first j cols of words
        dp = [[0] * (n + 1) for _ in range(t_len + 1)]
        dp[0][0] = 1  # Base case: one way to form empty target

        for i in range(t_len + 1):
            for j in range(n):
                if i > 0:
                    char_idx = ord(target[i - 1]) - ord('a')
                    dp[i][j + 1] = (dp[i][j + 1] + dp[i - 1][j] * freq[j][char_idx]) % MOD
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % MOD

        return dp[t_len][n]