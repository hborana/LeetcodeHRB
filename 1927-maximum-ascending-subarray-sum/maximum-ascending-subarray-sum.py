class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Edge case for empty list

        max_sum = nums[0]  # Maximum sum found
        curr_sum = nums[0]  # Sum of current ascending subarray

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Strictly increasing condition
                curr_sum += nums[i]  # Extend subarray
            else:
                max_sum = max(max_sum, curr_sum)  # Update max_sum if needed
                curr_sum = nums[i]  # Start a new subarray

        return max(max_sum, curr_sum)