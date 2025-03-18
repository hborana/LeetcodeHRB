class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        curr_or = 0  # Bitwise OR of elements in the window
        max_length = 0

        for right in range(len(nums)):
            # Ensure the new element doesn't violate the nice condition
            while (curr_or & nums[right]) != 0:
                curr_or ^= nums[left]  # Remove nums[left] from OR
                left += 1  # Shrink window

            # Add the current element to OR and update max_length
            curr_or |= nums[right]
            max_length = max(max_length, right - left + 1)

        return max_length