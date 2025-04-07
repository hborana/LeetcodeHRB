class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        

    def helper(self, nums):  ## House Rober 1 , ( can be used as a Helper )
        rob1, rob2 = 0,0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2