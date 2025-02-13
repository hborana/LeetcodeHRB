class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Convert nums into a min heap
        heapq.heapify(nums)
        operations = 0

        # Process while the smallest element is less than k
        while nums[0] < k:
            if len(nums) < 2:
                return -1  # This should not happen based on problem constraints
            
            # Extract two smallest elements
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            
            # Compute the new value
            new_val = x * 2 + y
            
            # Insert the new value into the heap
            heapq.heappush(nums, new_val)
            
            # Increment operation count
            operations += 1

        return operations