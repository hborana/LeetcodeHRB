class Solution:
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        cycle_length = 2 * (n - 1)
        remainder = time % cycle_length
        
        if remainder < n:
            return remainder + 1
        else:
            return n - (remainder - (n - 1))
        