class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        for i in range(n - 2):  # Stop at n-2 because we need 3 consecutive elements
            if nums[i] == 0:
                # Flip nums[i], nums[i+1], nums[i+2]
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                operations += 1

        # If any remaining 0s exist, return -1
        return operations if all(num == 1 for num in nums) else -1