class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum, min_sum = 0, 0
        current_max, current_min = 0, 0

        for num in nums:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        return max(max_sum, abs(min_sum))
            