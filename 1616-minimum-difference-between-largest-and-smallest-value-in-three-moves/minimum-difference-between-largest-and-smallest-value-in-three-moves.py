class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()
        scenario1 = nums[n - 1] - nums[3]      
        scenario2 = nums[n - 2] - nums[2]     
        scenario3 = nums[n - 3] - nums[1]      
        scenario4 = nums[n - 4] - nums[0]      

        return min(scenario1, scenario2, scenario3, scenario4)