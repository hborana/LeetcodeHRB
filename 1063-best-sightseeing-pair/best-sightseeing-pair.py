class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Initialize variables
        max_score = 0
        max_i_plus = values[0]  # Initially, values[0] + 0

        # Iterate through the array starting from the second element
        for j in range(1, len(values)):
            # Calculate score for the current pair (i, j)
            max_score = max(max_score, max_i_plus + values[j] - j)

            # Update max_i_plus to include the current j
            max_i_plus = max(max_i_plus, values[j] + j)

        return max_score
