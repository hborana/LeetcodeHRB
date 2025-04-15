class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
       
        total = 0
        for key in freq:
            if freq[key] == 1:
                total += key

        return total 