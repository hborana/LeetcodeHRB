class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_map = defaultdict(int)
        n = len(nums)
        count_tuples = 0

        # Count product occurrences
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1

        # Calculate valid tuple count
        for count in product_map.values():
            if count > 1:
                count_tuples += (count * (count - 1) // 2) * 8

        return count_tuples
            