class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}  # Dictionary to count occurrences of 'a', 'b', and 'c'
        left = 0
        result = 0
        
        for right in range(len(s)):  # Expand right pointer
            count[s[right]] += 1

            while all(count[ch] > 0 for ch in 'abc'):  # Check if window contains 'a', 'b', and 'c'
                result += len(s) - right  # All substrings from 'left' to end are valid
                count[s[left]] -= 1  # Shrink left pointer
                left += 1

        return result