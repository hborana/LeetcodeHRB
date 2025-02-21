class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        # Newton-Rapson Method 


        x = num
        while x * x > num:
            x = (x + num // x) // 2  # Integer division

        return x * x == num  # Check if it is a perfect square


        
        