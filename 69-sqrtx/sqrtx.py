class Solution:
    def mySqrt(self, x: int) -> int:
        # edge case 
        if x < 0:
            return "Invalid Input"
        
        if x == 0 or x == 1:
            return x

        n = x
        # Newton - Rapson Method for solving the problem 
        while x * x > n:
            x = (x + n // x ) // 2 

        
        return x 

        