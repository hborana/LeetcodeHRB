class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drops = 0

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                drops += 1
                if drops > 1:
                    return False

        # If no drops, it's already sorted
        if drops == 0:
            return True

        # Check if the last element is <= the first element
        return nums[-1] <= nums[0]
        