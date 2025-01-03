class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        prefix_sum = 0
        valid_splits = 0

        for i in range(n - 1):  # Ensure there's at least one element to the right of i
            prefix_sum += nums[i]
            suffix_sum = total_sum - prefix_sum
            if prefix_sum >= suffix_sum:
                valid_splits += 1

        return valid_splits