class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        # Initialize the moves counter
        moves = 0
        
        # Iterate through the sorted array and ensure each element is unique
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                # Calculate the increment needed to make nums[i] unique
                increment = nums[i - 1] - nums[i] + 1
                # Apply the increment
                nums[i] += increment
                # Add the increment to the total moves
                moves += increment
        
        return moves
