class Solution:
    def romanToInt(self, s: str) -> int:
        # Define the mapping of Roman numerals to integers
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        # Initialize the result integer
        result = 0
        
        # Iterate over the string from left to right
        for i in range(len(s)):
            # If the current numeral is less than the next one, subtract it from the result
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                # Otherwise, add it to the result
                result += roman_map[s[i]]
        
        return result
        