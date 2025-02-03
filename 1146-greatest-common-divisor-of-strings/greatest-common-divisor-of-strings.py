class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
         # Start with the shorter string as the initial candidate
        candidate = str1 if len(str1) < len(str2) else str2
        
        # Check for valid divisor by reducing the candidate string
        while candidate:
            if (len(str1) % len(candidate) == 0 and len(str2) % len(candidate) == 0 and
                str1 == candidate * (len(str1) // len(candidate)) and
                str2 == candidate * (len(str2) // len(candidate))):
                return candidate  # Found the largest valid repeating substring
            candidate = candidate[:-1]  # Remove the last character and try again
        
        return ""  # No common divisor found
            
            