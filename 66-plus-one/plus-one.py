class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Start from the least significant digit
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # Add one to the current digit
            if digits[i] < 10:
                return digits  # No carry, return the result
            digits[i] = 0  # Carry over, set to 0 and continue

        # If all digits were 9, we need to add a new digit at the front
        return [1] + digits