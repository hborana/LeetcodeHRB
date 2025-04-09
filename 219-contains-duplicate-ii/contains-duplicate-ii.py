class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, vl in enumerate(nums):
            if vl in seen and i - seen[vl] <= k:
                return True
            else:
                seen[vl] = i

        return False        