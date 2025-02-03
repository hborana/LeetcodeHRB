class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
         # Check if a valid common divisor pattern exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute the GCD of the lengths
        gcd_length = gcd(len(str1), len(str2))
        
        # Return the substring of length gcd_length from str1
        return str1[:gcd_length]
                
            