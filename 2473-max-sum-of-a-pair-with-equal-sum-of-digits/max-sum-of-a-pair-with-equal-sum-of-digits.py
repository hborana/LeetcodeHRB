class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(x):
            return sum(int(d) for d in str(x))
        
        sum_map = defaultdict(list)  # Stores the two largest numbers for each digit sum group
        max_sum = -1

        for num in nums:
            s = digit_sum(num)
            sum_map[s].append(num)
            sum_map[s] = sorted(sum_map[s], reverse=True)[:2]  # Keep only top 2 largest

        # Check max sum of valid pairs
        for key in sum_map:
            if len(sum_map[key]) > 1:
                max_sum = max(max_sum, sum_map[key][0] + sum_map[key][1])

        return max_sum