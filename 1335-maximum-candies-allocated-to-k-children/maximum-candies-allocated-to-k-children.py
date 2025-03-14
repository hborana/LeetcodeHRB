class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return 0

        left, right = 1, max(candies)
        best = 0
        
        while left <= right:
            mid = (left + right) // 2
            count = sum(c // mid for c in candies)
            
            if count >= k:  # If we can satisfy at least k children
                best = mid
                left = mid + 1  # Try for a larger `mid`
            else:
                right = mid - 1  # Reduce `mid`
        
        return best