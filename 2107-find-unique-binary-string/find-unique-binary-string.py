class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        num_set = set(nums)
        
        for i in range(2 ** n):  # Generate all possible binary numbers
            bin_str = format(i, f'0{n}b')  # Convert to n-length binary string
            if bin_str not in num_set:
                return bin_str
            