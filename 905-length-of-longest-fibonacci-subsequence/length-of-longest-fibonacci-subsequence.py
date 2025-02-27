class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}  # Map value to index
        dp = {}  # Dictionary to store (i, j) -> length
        max_len = 0

        for j in range(len(arr)):
            for i in range(j):
                x = arr[j] - arr[i]  # Check if arr[j] - arr[i] exists in arr
                if x in index and index[x] < i:
                    k = index[x]
                    dp[(i, j)] = dp.get((k, i), 2) + 1  # Update length
                    max_len = max(max_len, dp[(i, j)])

        return max_len if max_len >= 3 else 0 
            