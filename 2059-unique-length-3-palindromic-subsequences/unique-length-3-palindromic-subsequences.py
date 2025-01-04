class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict

        # Dictionary to track the first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}

        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        unique_palindromes = set()

        # Process each character as the potential center
        for char in first_occurrence:
            start = first_occurrence[char]
            end = last_occurrence[char]

            # Collect all unique characters between first and last occurrence
            if end - start > 1:  # There must be characters between
                for middle_char in set(s[start + 1:end]):
                    # Form the palindrome and add to the set
                    unique_palindromes.add(char + middle_char + char)

        # Return the count of unique palindromes
        return len(unique_palindromes)