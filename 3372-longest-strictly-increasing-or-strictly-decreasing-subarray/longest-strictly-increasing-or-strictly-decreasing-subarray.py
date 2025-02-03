class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case for empty list

        inc_len = 1  # Length of increasing subarray
        dec_len = 1  # Length of decreasing subarray
        max_len = 1  # Store the maximum length found

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Strictly increasing
                inc_len += 1
                dec_len = 1  # Reset decreasing length
            elif nums[i] < nums[i - 1]:  # Strictly decreasing
                dec_len += 1
                inc_len = 1  # Reset increasing length
            else:  # nums[i] == nums[i - 1] (reset both)
                inc_len = dec_len = 1

            max_len = max(max_len, inc_len, dec_len)  # Update max length

        return max_len
            