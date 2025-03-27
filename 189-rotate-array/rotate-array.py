class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # If rotation is greater 
        # than size of array
        n = len(nums)
        k %= n

        nums[:] = nums[-k:] + nums[:-k]  # Update the array in place
