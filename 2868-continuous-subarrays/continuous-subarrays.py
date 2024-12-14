from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        count = 0
        max_deque = deque()  # Monotonic deque for max values
        min_deque = deque()  # Monotonic deque for min values

        for right in range(n):
            # Add the new element to the max and min deques
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Ensure the window [left, right] satisfies the condition
            while nums[max_deque[0]] - nums[min_deque[0]] > 2:
                left += 1
                # Remove elements no longer in the window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Count subarrays ending at right
            count += (right - left + 1)

        return count
