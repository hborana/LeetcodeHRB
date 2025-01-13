class Solution:
    def minimumLength(self, s: str) -> int:
         # Step 1: Count the occurrences of each character in the string
        char_frequency_map = Counter(s)

        # Step 2: Calculate the total number of deletable characters
        deletable_count = 0
        for frequency in char_frequency_map.values():
            if frequency % 2 == 1:
                # For odd frequencies, delete all but one character
                deletable_count += frequency - 1
            else:
                # For even frequencies, delete all but two characters
                deletable_count += frequency - 2

        # Step 3: Compute the minimum length of the string after deletions
        return len(s) - deletable_count
            