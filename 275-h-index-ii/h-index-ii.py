class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n-1 

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                right = mid - 1  # Look for a larger h-index in the left half
            else:
                left = mid + 1  # Look in the right half
        
        return n - left
