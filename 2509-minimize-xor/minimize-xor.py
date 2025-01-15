class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count set bits in num2 (target number of 1s)
        target_set_bits_count = bin(num2).count('1')
        
        # Initialize result to 0
        result = 0
        
        # Step 1: Retain the most significant bits of num1
        for i in range(31, -1, -1):  # Iterate over 31 bits (0 to 31)
            if (num1 & (1 << i)) and target_set_bits_count > 0:
                result |= (1 << i)  # Set this bit in the result
                target_set_bits_count -= 1
        
        # Step 2: Add additional bits to match the target set bit count
        for i in range(32):  # Iterate over all bits again
            if target_set_bits_count == 0:
                break  # Stop if we have enough set bits
            if not (result & (1 << i)):  # If the bit is not set in result
                result |= (1 << i)  # Set this bit in the result
                target_set_bits_count -= 1
        
        return result