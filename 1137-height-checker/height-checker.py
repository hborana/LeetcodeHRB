class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)  # Sort heights to get the expected order
        count = 0  # Initialize the counter
        
        # Compare heights with expected
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1  # Increment the counter when there's a mismatch
        
        return count
        