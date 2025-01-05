class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        delta = [0] * (n + 1)  # Extra space to handle the end boundary

        # Process shifts and update delta array
        for start, end, direction in shifts:
            if direction == 1:  # Forward shift
                delta[start] += 1
                delta[end + 1] -= 1
            else:  # Backward shift
                delta[start] -= 1
                delta[end + 1] += 1

        # Calculate prefix sum of delta to determine net shifts
        net_shift = 0
        result = []

        for i in range(n):
            net_shift += delta[i]
            # Normalize the shift within the range of 26 letters
            effective_shift = net_shift % 26
            # Apply the shift
            new_char = chr((ord(s[i]) - ord('a') + effective_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)