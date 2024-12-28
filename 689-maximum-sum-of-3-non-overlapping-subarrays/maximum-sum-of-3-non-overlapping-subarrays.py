class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: Calculate sum of each subarray of length k
        subarray_sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        subarray_sums[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            subarray_sums[i] = current_sum

        # Step 2: Calculate best left indices
        best_left = [0] * len(subarray_sums)
        best = 0
        for i in range(len(subarray_sums)):
            if subarray_sums[i] > subarray_sums[best]:
                best = i
            best_left[i] = best

        # Step 3: Calculate best right indices
        best_right = [0] * len(subarray_sums)
        best = len(subarray_sums) - 1
        for i in range(len(subarray_sums) - 1, -1, -1):
            if subarray_sums[i] >= subarray_sums[best]:  # Prefer lexicographically smaller
                best = i
            best_right[i] = best

        # Step 4: Evaluate all possible middle subarrays
        max_sum = 0
        result = []
        for middle in range(k, len(subarray_sums) - k):
            left = best_left[middle - k]
            right = best_right[middle + k]
            total = subarray_sums[left] + subarray_sums[middle] + subarray_sums[right]
            if total > max_sum:
                max_sum = total
                result = [left, middle, right]
            elif total == max_sum and [left, middle, right] < result:
                result = [left, middle, right]

        return result
