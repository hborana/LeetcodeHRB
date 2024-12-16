class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            small_no = nums.index(min(nums))
            nums[small_no] *= multiplier
        
        return nums 