class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)

        # Iterate over possible lengths of substrings, starting from longest
        for length in range(n, 0, -1):
            substring_count = {}

            # Generate substrings of the current length
            for i in range(n - length + 1):
                substring = s[i:i+length]

                # Check if the substring is special (all characters are the same)
                if len(set(substring)) == 1:
                    substring_count[substring] = substring_count.get(substring, 0) + 1
            
            # Check if any substring occurs at least three times
            if any(count >= 3 for count in substring_count.values()):
                return length
        
        # If no such substring is found, return -1
        return -1