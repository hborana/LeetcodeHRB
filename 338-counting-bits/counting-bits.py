class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # Count of 1's in i is 1 + count of 1's in i & (i - 1)
            ans[i] = ans[i & (i - 1)] + 1
        
        return ans