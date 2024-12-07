class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        def canAchievePenalty(penalty):
            operations = 0
            for balls in nums:
                if balls > penalty:
                    # Number of splits required to make balls <= penalty
                    operations += (balls - 1) // penalty
            return operations <= maxOperations

        # Binary search for the minimum penalty
        left, right = 1, max(nums)
        result = right  # Initialize with the largest possible penalty

        while left <= right:
            mid = (left + right) // 2
            if canAchievePenalty(mid):
                result = mid  # Update result and try for a smaller penalty
                right = mid - 1
            else:
                left = mid + 1
        
        return result