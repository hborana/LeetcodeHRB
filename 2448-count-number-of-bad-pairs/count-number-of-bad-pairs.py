class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        good_pairs = 0
        n = len(nums)

        for j in range(n):
            key = nums[j] - j
            good_pairs += freq_map[key]  # Count good pairs that match (nums[i] - i)
            freq_map[key] += 1  # Store the occurrence

        total_pairs = (n * (n - 1)) // 2  # Total possible pairs
        return total_pairs - good_pairs  