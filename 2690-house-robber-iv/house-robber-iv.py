class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob_with_capability(x):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= x:  # If this house can be robbed under current capability
                    count += 1
                    i += 1  # Skip next house (adjacency rule)
                i += 1
            return count >= k

        left, right = min(nums), max(nums)
        while left < right:
            mid = (left + right) // 2
            if can_rob_with_capability(mid):
                right = mid  # Try to find a smaller valid capability
            else:
                left = mid + 1  # Increase capability since `mid` is too small
        return left