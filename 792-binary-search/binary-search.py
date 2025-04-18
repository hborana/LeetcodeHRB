class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ##Base case. 

        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if left > 0 and nums[left - 1] == target:
            return left - 1
        return -1
            