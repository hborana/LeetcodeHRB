class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Count the total number of ones in the string
        total_ones = s.count('1')
        max_score = 0
        zeros_in_left = 0
        ones_in_right = total_ones

        # Iterate through the string, excluding the last character
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_in_left += 1
            else:
                ones_in_right -= 1
            # Calculate the current score
            current_score = zeros_in_left + ones_in_right
            # Update the maximum score if the current score is higher
            max_score = max(max_score, current_score)

        return max_score