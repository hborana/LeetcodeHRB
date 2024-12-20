class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Phase 1: Find the candidate for majority element
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Phase 2: Return the candidate
        return candidate

        