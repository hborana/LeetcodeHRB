class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        mods = {0: -1}  # Initialize with 0: -1 to handle subarrays starting from index 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            mod = prefix_sum % k
            
            if mod in mods:
                if i - mods[mod] > 1:  # Ensure the subarray length is at least 2
                    return True
            else:
                mods[mod] = i  # Store the first occurrence of this mod
            
        return False
        